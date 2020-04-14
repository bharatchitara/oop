#from builtins import None
class Parrot:
    __counter=7000
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
        self.__unique_number=Parrot.__counter+1
        Parrot.__counter+=1

    def get_name(self):
        return self.__name


    def get_color(self):
        return self.__color


    def get_unique_number(self):
        
        return self.__unique_number


#     def set_name(self, value):
#         self.__name = value
# 
# 
#     def set_color(self, value):
#         self.__color = value
# 
# 
#     def set_unique_id(self, value):
#         self.__unique_id = value




p1=Parrot('a','red')
print(p1.get_name())
print(p1.get_color())
print(p1.get_unique_number())
p2=Parrot('b','red')
print(p2.get_name())
print(p2.get_color())
print(p2.get_unique_number())