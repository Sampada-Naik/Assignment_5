from socket import getnameinfo

from matplotlib.pyplot import title
from sklearn.metrics import balanced_accuracy_score

#Challenge 1
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        add = self.num1 + self.num2
        print(add)

    def subtraction(self):
        sub = self.num1 - self.num2
        sub1 = abs(sub)
        print(sub1)

    def multiplication(self):
        mul = self.num1 * self.num2
        print(mul)

    def division(self):
        div = self.num1 / self.num2
        print(div)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
object = Calculator(num1,num2)
object.addition()
object.subtraction()
object.multiplication()
object.division()

# Challenge 3
class Students:
    def _init_(self):
        self.__name = name
        self.__rollnumber = rollnumber
    #setter
    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self,rollnumber):
        self.__rollnumber = rollnumber

    def getRollNumber(self):
        return self.__rollnumber

student_obj = Students()
name = input("Enter the student name: ")
rollnumber = int(input("Enter the student roll number: "))
student_obj.setName(name)
print(student_obj.getName())
student_obj.setRollNumber(rollnumber)  
print(student_obj.getRollNumber())  
