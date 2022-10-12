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
