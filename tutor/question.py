from tags import QuestionType, Difficulty


def add_underline(length=1):
    return r'\underline{\hspace{' + str(length) + 'cm}}'


def include_graphs(graphs, width=5, newline=True):
    if not graphs:
        return ''
    gs = '\n'.join([r'\includegraphics[width=' + str(width) + 'cm]{' + gname + '}' for gname in graphs])
    if newline:
        gs = r'\newline ' + gs
    return gs


class Question:
    def __init__(self, question_type, question, grade, area, term=None, choices=None, graphs=None, source=None,
                 difficulty=None, thoughts=None, answer=None):
        self.question_type = question_type
        self.question = question
        self.grade = grade
        self.area = area
        self.term = term
        self.choices = choices
        self.graphs = graphs
        self.source = source  # 题目来源
        self.difficulty = difficulty
        self.thoughts = thoughts  # 典型思路，list of thought enum
        self.answer = answer

    def to_tex(self, graph_width=5):
        raise Exception('Base class')


class MultipleChoiceQuestion(Question):
    # 选择题
    def __init__(self, question, grade, area, term=None, choices=None, graphs=None, source=None, difficulty=None,
                 thoughts=None, answer=None):
        super().__init__(QuestionType.MultipleChoice, question, grade, area, term=term, choices=choices, graphs=graphs,
                         source=source, difficulty=difficulty, thoughts=thoughts, answer=answer)

    def to_tex(self, graph_width=5):
        choices = ''.join([r'\item ' + c for c in self.choices])
        tex = (r'\begin{question}' + self.question + r'\paren\begin{choices}' + choices +
               include_graphs(self.graphs, graph_width) + r'\end{choices}\end{question}')
        return tex


class TrueFalseQuestion(Question):
    # 判断题
    def __init__(self, question, grade, area, term=None, graphs=None, source=None, difficulty=None, thoughts=None,
                 answer=None):
        super().__init__(QuestionType.TrueFalse, question, grade, area, term=term, graphs=graphs, source=source,
                         difficulty=difficulty, thoughts=thoughts, answer=answer)

    def to_tex(self, graph_width=5):
        tex = r'\begin{question}' + self.question + include_graphs(self.graphs, graph_width) + r'\paren\end{question}'
        return tex


class FillInBlankQuestion(Question):
    # 填空题
    def __init__(self, question, grade, area, term=None, graphs=None, source=None, difficulty=None, thoughts=None,
                 answer=None):
        super().__init__(QuestionType.FillInBlanks, question, grade, area, term=term, graphs=graphs, source=source,
                         difficulty=difficulty, thoughts=thoughts, answer=answer)

    def to_tex(self, graph_width=5):
        tex = r'\begin{question}' + self.question + include_graphs(self.graphs, graph_width) + r'\end{question}'
        return tex


class ShortAnswerQuestion(Question):
    # 简答题
    def __init__(self, question, grade, area, term=None, graphs=None, source=None, difficulty=None, thoughts=None,
                 answer=None):
        super().__init__(QuestionType.ShortAnswer, question, grade, area, term=term, graphs=graphs, source=source,
                         difficulty=difficulty, thoughts=thoughts, answer=answer)

    def to_tex(self, graph_width=5):
        tex = r'\begin{problem}' + self.question + include_graphs(self.graphs, graph_width) + r'\end{problem}'
        return tex


if __name__ == '__main__':
    from tags import Grade, Area
    q = MultipleChoiceQuestion('题干', Grade.Four, area=Area.Geometry, choices=['选项1', '选项2', '选项3'])
    print(q.to_tex())
