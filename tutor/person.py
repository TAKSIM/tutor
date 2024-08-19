from tags import Gender, Role


class Person:
    def __init__(self, name, role, gender, address, birth_year=None, birth_month=None, birth_day=None,
                 mobile=None, china_id=None, email=None):
        self.name = name
        self.role = role
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.gender = gender
        self.address = address
        self.mobile = mobile
        self.china_id = china_id
        self.email = email


Family_1 = [
    Person('赵一涵', Role.Student, Gender.Female, '富兴首府502', birth_year=2014, birth_month=8, birth_day=11,
           mobile='13722666228', china_id='37092320140811254X'),
    Person('谷香存', Role.Parent, Gender.Female, '富兴首府502', birth_year=1989, birth_month=10, birth_day=4,
           mobile='15911117686', china_id='371522198910048422')
]

Family_2 = [
    Person('路丁康', Role.Student, Gender.Female, '富兴首府902', birth_year=2001),
    Person('梅', Role.Parent, Gender.Female, '富兴首府902')
]