"""University Management System - Core Logic"""


class CurseFullError(Exception):
    pass

class AllReadyEnrollesError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
    def __repr__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Age: {self.age})"

class Professor:
    def __init__(self, professor_id, name):
        self.professor_id = professor_id
        self.name = name
        self.teaching_subjects = []
    def __repr__(self):
        return f"Professor(ID: {self.professor_id}, Name: {self.name})"

class Course:
    def __init__(self, course_id, name, professor,max_capacity):
        self.course_id = course_id
        self.name = name
        self.professor = professor
        self.students = []
        self.max_capacity = max_capacity
    def __repr__(self):
        return f"Course(ID: {self.course_id}, Name: {self.name}, Professor: {self.professor.name})"


class University:
    def __init__(self):
        self.students = {}
        self.professors = {}
        self.courses = {}

    def add_student(self, student):

        self.students[student.student_id] = student

    def add_professor(self, professor):
        self.professors[professor.professor_id] = professor


    def add_course(self, course):
        if course.professor is None:
            raise Exception("Course must have a professor assigned.")
        self.courses[course.course_id] = course
        course.professor.teaching_subjects.append(course)


    def enroll_student_in_course(self, student_id, course_id):
        student = self.students[student_id]
        course = self.courses[course_id]

        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            raise StudentNotFoundError(f"Student with ID {student_id} does not exist.")
        if course_id not in self.courses:
            print(f"Course with ID {course_id} does not exist.")
            raise Exception(f"Course with ID {course_id} does not exist.")
        if student in course.students:
            print(f"Student {student.name} is already enrolled in course {course.name}.")
            raise AllReadyEnrollesError(f"Student {student.name} is already enrolled in course {course.name}.")

        if len(course.students) >= course.max_capacity:
            print(f"Course {course.name} is at full capacity.")
            raise CurseFullError(f"Course {course.name} is at full capacity.")

        course.students.append(student)
        student.courses.append(course)

    def remove_student(self, student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            raise StudentNotFoundError(f"Student with ID {student_id} does not exist.")
        student = self.students[student_id]
        for course in student.courses:
            course.students.remove(student)
        del self.students[student_id]

    def get_student_courses(self, student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            raise StudentNotFoundError(f"Student with ID {student_id} does not exist.")

        student = self.students[student_id]
        return student.courses

    def get_course_students(self, course_id):
        if course_id not in self.courses:
            print(f"Course with ID {course_id} does not exist.")
            raise Exception(f"Course with ID {course_id} does not exist.")

        course = self.courses[course_id]
        return course.students


    def sort_students_by_id(self):
        return sorted(self.students.values(), key=lambda student: student.student_id)

    def sort_students_by_name(self):
        return sorted(self.students.values(), key=lambda student: student.name)

    def search_student_by_name(self, keyword):
        return [student for student in self.students.values() if student.name.lower() == keyword.lower()]

    def most_popular_course(self):
        if not self.courses:
            return None
        return max(self.courses.values(), key=lambda course: len(course.students))

uni = University()
stud1 = Student(1, "Alice", 20)
prof1 = Professor(1, "Dr. Smith")
cour1 = Course(1, "Math 101", prof1, 30)

stud2 = Student(2, "Bob", 22)
prof2 = Professor(2, "Dr. Johnson")
cour2 = Course(2, "Physics 101", prof2, 25)

uni.add_student(stud1)
uni.add_student(stud2)

uni.add_professor(prof2)
uni.add_professor(prof1)


uni.add_course(cour1)
uni.add_course(cour2)

uni.enroll_student_in_course(1, 1)

uni.sort_students_by_name()
print(uni.sort_students_by_name())

uni.most_popular_course()
print(uni.most_popular_course())

uni.get_course_students(1)
print(uni.get_course_students(1))

uni.get_student_courses(1)
print(uni.get_student_courses(1))

uni.search_student_by_name("Anahit")
print(uni.search_student_by_name("Anahit"))








