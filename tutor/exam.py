import os


class Exam:
    def __init__(self, title, subject, questions=None):
        self.title = title
        self.subject = subject
        self.questions = questions

    def tex_title(self):
        return r'\title{' + self.title + '}'

    def tex_subject(self):
        return r'\subject{' + self.subject + '}'

    def doc_begin(self):
        return (r'''
        \documentclass{exam-zh}
        \usepackage{siunitx}
        \examsetup{
          page/size=a4paper,
          paren/show-paren=true,
          paren/show-answer=false,
          fillin/show-answer=false,
          solution/show-solution=false
        }
        \ExamPrintAnswerSet{
          sealline/show=true,
          page/size=a3paper,
          paren/show-answer=false,
          fillin/show-answer=false,
          solution/show-solution=false,
        }
        \everymath{\displaystyle}
        ''' + self.tex_title() + self.tex_subject() + r'\begin{document}\maketitle')

    def doc_end(self):
        return r'\end{document} '

    def to_tex(self, file_name=None):
        fn = file_name or 'exam.tex'
        fp = os.path.join(os.getcwd(), 'latex', fn)
        tex = self.doc_begin() + ''.join([q.to_tex() for q in self.questions]) + self.doc_end()
        with open(fp, 'w', encoding='utf-8') as file:
            file.write(tex)


if __name__ == '__main__':
    from question_set import get_question
    import pandas as pd
    from tags import Grade, Term
    exam = Exam('路丁康 初一下学期', '错题汇总')
    grade = Grade.Seven
    term = Term.Second
    qset = pd.read_pickle(r'D:\pwrd\code\tutor\ludingkang\ldk')
    qs = [get_question(qdata) for _, qdata in qset.iterrows()]
    exam.questions = qs
    exam.to_tex(r'D:\pwrd\code\tutor\ludingkang\ldk.tex')

