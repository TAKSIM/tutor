from enum import Enum


class Grade(Enum):
    One = '一年级'
    Two = '二年级'
    Three = '三年级'
    Four = '四年级'
    Five = '五年级'
    Six = '六年级'
    Seven = '初一'
    Eight = '初二'
    Nine = '初三'
    Ten = '高一'
    Eleven = '高二'
    Twelve = '高三'


class Term(Enum):
    First = '上学期'
    Second = '下学期'


class Area(Enum):
    # https://en.m.wikipedia.org/wiki/Mathematics
    NumberTheory = '数论'
    Geometry = '几何'
    Algebra = '代数'
    Combinatorics = '组合'
    Logic = '逻辑'
    Statistics = '统计'
    Calculus = '分析'

    # 适用于小学一些过于基础的题目，比如计数体系和四则混合运算
    Basic = '初级'


class QuestionType(Enum):
    TrueFalse = '判断题'
    MultipleChoice = '选择题'
    FillInBlanks = '填空题'
    ShortAnswer = '解答题'


class Difficulty(Enum):
    Hard = '难'
    OK = '中等'
    EASY = '简单'


class Thoughts(Enum):
    Extreme = '极端值'
    CongruentTriangular = '全等三角形'


class Gender(Enum):
    Male = '男'
    Female = '女'


class Role(Enum):
    Student = '学生'
    Parent = '家长'

