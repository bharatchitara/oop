class Instructor:
    def __init__(self):
         
        self.__instructor_name=None
        self.__technology_skill = []
        self.__experience = None
        self.__avg_feedback= None
        self.technology=None
        self.value=None
 
    def get_instructor_name(self):
        return self.__instructor_name
 
 
    def get_technology_skill(self):
        return self.__technology_skill
 
 
    def get_experience(self):
        return self.__experience
 
 
    def get_avg_feedback(self):
        return self.__avg_feedback
 
 
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
 
 
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
 
 
    def set_experience(self, experience):
        self.__experience = experience
 
 
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
 
     
    def check_eligibility(self):
        if self.__experience>3 and self.__avg_feedback >=4.5:
            return True
        elif self.__experience<=3 and self.__avg_feedback>=4:
            return True
        else:
            return False
             
     
    def allocate_course(self,technology):
    
        for self.value in self.__technology_skill:
            if(self.value in self.__technology_skill and self.check_eligibility()==1 ):
             
                return True
            else:
                return False
             
 
c1= Instructor()
c1.set_instructor_name("bharat")
c1.set_technology_skill(['JAVA','PYTHON'])
c1.set_experience(2)
c1.set_avg_feedback(4.6)
print(c1.check_eligibility())
print(c1.allocate_course('python'))













# class Instructor :
#     def _init_(self):
#         self.__instructor_name = None 
#         self.__experience = None 
#         self.__avg_feedback = None
#         self.__technology_skill = None
#     
#     def set_technology_skill(self , technology_skill) :
#         self.__technology_skill = technology_skill
#     def set_instructor_name(self ,instructor_name) :
#         self.__instructor_name = instructor_name
#     def set_experience(self , experience):
#         self.__experience = experience
#     def set_avg_feedback(self , avg_feedback):
#         self.__avg_feedback = avg_feedback 
#     def get_instructor_name(self) :
#         return self.__instructor_name 
#     def get_experience(self ):
#         return self.__experience 
#     def get_avg_feedback(self ):
#         return self.__avg_feedback 
#     def get_technology_skill(self ) :
#         return self.__technology_skill 
#     def check_eligibility(self):
#         if self.__experience > 3 and self.__avg_feedback >= 4.5 :
#             return True
#         elif self.__experience <= 3 and self.__avg_feedback >= 4 :
#             return True
#         else :
#             return False
#         
#     def allocate_course(self,technology):
#         if technology in self.__technology_skill and self.check_eligibility():
#             return True 
#         else :
#             return False
#         
# instructor_1 = Instructor()
# technology_skills = ['python' , 'java' , 'c' , 'sql']
# instructor_1.set_technology_skill(technology_skills)
# 
# instructor_1.set_instructor_name("prasanna") 
# instructor_1.set_experience(5)
# instructor_1.set_avg_feedback(4.5)
# print(instructor_1.check_eligibility())
# print(instructor_1.allocate_course('python'))
