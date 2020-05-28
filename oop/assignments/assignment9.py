#OOPR-Assgn-8
#Start writing your code here
#from __builtin__ import True, None

class Student:
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
        self.__course_id=None
        self.__fees=None
        self.course_id=[1001,1002]
        

    def get_course_id(self):
        return self.__course_ida


    def get_fees(self):
        return self.__fees


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
        if(self.validate_age()==1 and self.validate_marks()==1 and self.__marks>=65):
            
            return True
        else:
            return False
        
    def choose_course(self,course_id):
        if(self.check_qualification()==1):
            
            if(course_id==1001):
                if(self.__marks>85):
                    self.__fees = 25575*(0.75)
                    return self.__fees
                else:
                    self.__fees = 25575
                    return self.__fees
                
            elif(course_id==1002):
            
                if(self.__marks>85):
                    self.__fees = 15500*(0.75)
                    return self.__fees
                else:
                    self.__fees = 15500
                    return self.__fees
            else:
                return False

c1=Student()
c1.set_student_id('s-101')
c1.set_age(21)
c1.set_marks(65)
print(c1.validate_marks())
print(c1.validate_age())
print(c1.check_qualification())    
print(c1.choose_course(1002))



