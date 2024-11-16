class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, {self.age} years old, {self.student_id})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __hash__(self):
        return hash(self.student_id)


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = set()

    def add_student(self, student):
        self.students.add(student)

    def delete_student(self, last_name):
        student_to_remove = None
        for student in self.students:
            if student.last_name == last_name:
                student_to_remove = student
                break
        if student_to_remove:
            self.students.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __repr__(self):
        return f"Group {self.group_name} with students: {', '.join(str(student) for student in self.students)}"


# Приклад використання:
st1 = Student('Male', 30, 'Steve', 'Jobs', 'IT')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'IT2')
gr = Group('Piton IT')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('work') == st1
assert gr.find_student('work') is None

gr.delete_student('Taylor')
