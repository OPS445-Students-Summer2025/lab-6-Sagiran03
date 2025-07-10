#!/usr/bin/env python3

# Author ID: [ssuresh14]



class Student:



    # Constructor method, called when creating a Student object

    def __init__(self, name, number):

        self.name = name        # Store student name

        self.number = number    # Store student ID number as string

        self.courses = {}       # Initialize an empty dictionary for courses and grades



    # Method to display student name and number

    def displayStudent(self):

        print('Student Name: ' + self.name)

        print('Student Number: ' + self.number)



    # Method to add a course and its grade to the student's record

    def addGrade(self, course, grade):

        self.courses[course] = grade



    # Method to calculate and display GPA

    def displayGPA(self):

        gpa = 0.0

        for course in self.courses.keys():

            gpa += self.courses[course]  # Add all grades

        print('GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses)))



# Create a Student object

student1 = Student('John', '025969102')



# Display student info

student1.displayStudent()



# Add some grades

student1.addGrade('Math', 85)

student1.addGrade('Science', 90)

student1.addGrade('History', 78)



# Display GPA

student1.displayGPA()
