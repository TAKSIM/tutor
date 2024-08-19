# 一类题目的集合，比如赵一涵的错题，或者有意思的思维题目
import os
import pandas
from question import TrueFalseQuestion, FillInBlankQuestion, ShortAnswerQuestion, MultipleChoiceQuestion
from tags import QuestionType, Difficulty, Thoughts

set_cols = ['题型', '年级', '学期', '领域', '来源', '题干', '图片', '选项', '难度', '思路', '答案']


def save_question(qset, q):
    if os.path.isfile(qset):
        qs = pandas.read_pickle(qset)
    else:
        qs = pandas.DataFrame(columns=set_cols)
    graph_string = q.graphs and '|'.join(q.graphs) or ''
    choice_string = q.choices and '|'.join(q.choices) or ''
    thought_string = q.thoughts and '|'.join([t.value for t in q.thoughts]) or ''
    data = [q.question_type, q.grade, q.term, q.area, q.source, q.question, graph_string, choice_string, q.difficulty,
            thought_string, q.answer]
    qs.loc[len(qs.index)] = data
    qs.to_pickle(qset)


def get_question(qdata):
    q_type = qdata['题型']
    grade = qdata['年级']
    term = qdata['学期']
    area = qdata['领域']
    source = qdata['来源']
    question = qdata['题干']
    graphs = qdata['图片'] and qdata['图片'].split('|') or None
    choices = qdata['选项'] and qdata['选项'].split('|') or None
    difficulty = qdata['难度'] and Difficulty(qdata['难度']) or None
    thoughts = qdata['思路'] and [Thoughts(t) for t in qdata['思路'].split('|')] or None
    answer = qdata['答案']

    if q_type == QuestionType.ShortAnswer:
        return ShortAnswerQuestion(question, grade, area, term, graphs, source, difficulty, thoughts, answer)
    elif q_type == QuestionType.MultipleChoice:
        return MultipleChoiceQuestion(question, grade, area, term, choices, graphs, source, difficulty, thoughts, answer)
    elif q_type == QuestionType.TrueFalse:
        return TrueFalseQuestion(question, grade, area, term, graphs, source, difficulty, thoughts, answer)
    elif q_type == QuestionType.FillInBlanks:
        return FillInBlankQuestion(question, grade, area, term, graphs, source, difficulty, thoughts, answer)


if __name__ == '__main__':
    from tags import Grade, Term, Difficulty, Area
    question = r'满足$\sqrt{3}<x<\sqrt{17}$的整数共有'
    choices = ['1个', '2个', '3个', '4个']
    area = Area.Basic
    source = '错题'
    grade = Grade.Seven
    term = Term.Second
    difficulty = Difficulty.EASY
    answer = 'D'
    q = MultipleChoiceQuestion(question, grade, area, term=term, choices=choices, source=source, difficulty=difficulty,
                               answer=answer)
    save_question(r'D:\pwrd\code\tutor\ludingkang\ldk', q)
