# Day 12 Problem - Inheritance 

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = id
        self.scores = scores

    def calculate(self):
        self.average = sum(self.scores) / len(self.scores)
        if 90 <= self.average <= 100:
            return "O"
        elif 80 <= self.average < 90:
            return "E"
        elif 70 <= self.average < 80:
            return "A"
        elif 55 <= self.average < 70:
            return "P"
        elif 40 <= self.average < 55:
            return "D"
        elif self.average < 40:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())