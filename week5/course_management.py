class user:
    def __init__(self, name):
        self.name = name


class student(user):
    def __init__(self, name, grade, age):
        super().__init__(name)
        self.grade = grade
        self.age = age
        self.courses = []

    def display(self):
        return f"Name: {self.name}, Grade: {self.grade}, Age: {self.age}"

    def add_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses


class addCourse(user):
    def __init__(self, course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher

    def get_details(self):
        return f"Course: {self.course_name}, Course Code: {self.course_code}, Teacher: {self.teacher.get_details()}"


class teacher(user):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}, Subject: {self.subject}"


s1 = student("Abebe", 4.0, 21)
print(s1.display())

english = addCourse("English", 1021, teacher("Mr. Johnson", "English"))
math = addCourse("Math", "MAT101", teacher("Mr. Smith", "Math"))

s1.add_course(english)
s1.add_course(math)

for course in s1.get_courses():
    print(course.get_details())

