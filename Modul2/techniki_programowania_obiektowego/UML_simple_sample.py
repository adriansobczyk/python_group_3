class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id


class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def get_course_name(self):
        return self.course_name

    def get_course_code(self):
        return self.course_code


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course



'''
UML diagram

+---------------------+     +---------------------+     +-----------------------+
|       Person        |     |       Student       |     |        Teacher        |
+---------------------+     +---------------------+     +-----------------------+
| - name: str         |     | - student_id: int   |     | - employee_id: int    |
| - age: int          |     +---------------------+     +-----------------------+
+---------------------+              |                              |
| + get_name(): str   |              |                              |
| + get_age(): int    |              |                              |
+---------------------+              |                              |
                                     |                              |
                                     |                              |
                                     |                              |
                          +----------+-----------+                  |
                          |                      |                  |
                          |     Enrollment       |                  |
                          |                      |                  |
                          +----------------------+                  |
                          | - student: Student   |                  |
                          | - course: Course     |                  |
                          +----------------------+                  |
                          | + get_student(): Student                |
                          | + get_course(): Course                  |
                          +-----------------------------------------+

'''