class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} years old'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f', record book: {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = []

    def add_student(self, student):
        self.group.append(student)

    def delete_student(self, last_name):
        self.group = [s for s in self.group if s.last_name != last_name]

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'



st1 = Student('Male', 30, 'Steve', 'Jobs', 'History')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'Philosophy')
gr = Group('1')


gr.add_student(st1)
gr.add_student(st2)
print(gr)


assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')