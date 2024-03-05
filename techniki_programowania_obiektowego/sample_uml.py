class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, surname, age, student_id):
        super().__init__(name, surname, age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id


class Teacher(Person):
    def __init__(self, name, surname, age, teacher_id):
        super().__init__(name, surname, age)
        self.teacher_id = teacher_id

    def get_teacher_id(self):
        return self.teacher_id


class School:
    def __init__(self, name, students, teachers):
        self.name = name
        self.students = students
        self.teachers = teachers

    def get_name(self):
        return self.name

    def get_students(self):
        return self.students

    def get_teachers(self):
        return self.teachers