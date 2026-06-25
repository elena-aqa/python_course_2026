class Student:

    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade


student = Student("Helen", "Yeresko", 35, 95)

print(
    f"Name: {student.first_name}, "
    f"Surname: {student.last_name}, "
    f"Age: {student.age}, "
    f"Average grade: {student.average_grade}"
)

student.change_average_grade(100)

print(
    f"Name: {student.first_name}, "
    f"Surname: {student.last_name}, "
    f"Age: {student.age}, "
    f"Average grade: {student.average_grade}"
)