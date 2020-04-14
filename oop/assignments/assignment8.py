#OOPR-Assgn-8
#Start writing your code here
#from __builtin__ import True

class Student:
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None

    def get_student_id(self):
        return self.__student_id


    def get_age(self):
        return self.__age


    def get_marks(self):
        return self.__marks


    def set_student_id(self, student_id):
        self.__student_id = student_id


    def set_age(self, age):
        self.__age = age


    def set_marks(self, marks):
        self.__marks = marks


    def validate_marks(self):
        if(self.__marks>=0 and self.__marks<=100):
            return True
        else:
            return False
    
    def validate_age(self):
        if(self.__age>20 and self.__age<=100):
            return True
        else:
            return False
    
    def check_qualification(self):
        if(self.validate_age()==1 and self.validate_marks()==1):
            if(self.__marks>=65):
                return True
            else:
                return False
        else:
            return False

c1=Student()
c1.set_student_id('s-101')
c1.set_age(23)
c1.set_marks(70)
print(c1.validate_marks())
print(c1.validate_age())
print(c1.check_qualification())    