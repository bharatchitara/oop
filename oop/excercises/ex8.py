# #OOPR-Exer-8
# class Juggler:
#     def __init__(self,name):
#         self.__name=name
#  
#     def juggles(self,JugglingItem):
#         print( JugglingItem.get_name(self))
#         #write the code to make the juggler juggle
#  
# class JugglingItem:
#     def __init__(self,name):
#         self.__name=name
#  
#     def get_name(self):
#         return self.__name
#      
# j= Juggler("mark")
# j1=JugglingItem("Ball")
# j.juggles("Ball")

 
class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,jugglingitem):
        print(self.__name,'is juggling with',jugglingitem.get_name())

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
j=Juggler('Mark')
j1=JugglingItem('Ball')
j.juggles(j1)