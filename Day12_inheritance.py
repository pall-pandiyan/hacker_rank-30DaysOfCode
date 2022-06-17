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
    def __init__(self, fName, lName, idNo, scores):
        super().__init__(fName, lName, idNo)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    def calculate(self):
        n = len(self.scores)
        avg = sum(self.scores)/n
        if avg>= 90 and avg<=100:
            return 'O'
        elif avg>=80 and avg<90:
            return 'E'
        elif avg>=70 and avg<80:
            return 'A'
        elif avg>=55 and avg<70:
            return 'P'
        elif avg>=40 and avg<55:
            return 'D'
        elif avg>=0 and avg<40:
            return 'T'
    #
    # Write your function here
    def printPerson(self):
        super().printPerson()
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())