class StudentLimitException(Exception):

    def __init__(self, message="limit is reached"):
        self.message = message
        super().__init__(self.message)


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise StudentLimitException()
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def __str__(self):
        return f"Grup {self.name}: " + ", ".join(str(student) for student in self.students)

students = [
    Student("Andrii", "Shevchenko"),
    Student("Olia", "Kravchuk"),
    Student("Petro", "Ivanov"),
    Student("Iryna", "Kovalenko"),
    Student("Mykola", "Petrenko"),
    Student("Viktoria", "Saienko"),
    Student("Anton", "Bondarenko"),
    Student("Nadiia", "Tkachenko"),
    Student("Oleksii", "Pavlenko"),
    Student("Alina", "Dovzhenko"),
    Student("Yurii", "Shapoval")
]

group = Group("ІТ")

try:
    for student in students:
        group.add_student(student)
except StudentLimitException as e:
    print(e)

print(group)