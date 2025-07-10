#!/usr/bin/env python3
# Author ID: ssuresh14  # <-- Replace with your actual Seneca ID

class Student:

    # Accepts string for name and ensures number is stored as string
    def __init__(self, name, number):
        self.name = str(name)
        self.number = str(number)  # Fix #1: Ensure number is stored as a string
        self.courses = {}

    # Display student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Display GPA with ZeroDivisionError handling
    def displayGPA(self):
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'  # Fix #2: Avoid divide-by-zero
        gpa = 0.0
        for course in self.courses:
            gpa += self.courses[course]
        return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))

    # Display only passed courses (grade not 0.0)
    def displayCourses(self):
        passed_courses = []
        for course, grade in self.courses.items():
            if grade > 0.0:
                passed_courses.append(course)
        return passed_courses

if __name__ == '__main__':
    # Create first student and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student and add grades
    student2 = Student('Jessica', 123456)  # number passed as int — will be converted

    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display info for both
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
