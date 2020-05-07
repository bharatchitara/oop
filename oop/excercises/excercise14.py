

class VehicleService(Exception):
    def __init__(self,mechanic_list):
        self.__mechanic_list = mechanic_list
        
    def assign_vehicle_for_service(self,mechanic_id,vehicle_type):
        i,j=0
        if(i not in self.__mechanic_id):
            raise "InvalidMechanicIdException"
        
        for key in range(len(specialization_list)):
            
            if(key not in self.__vehicle_type):
                raise "InvalidMechanicSpecializationException"
            
            else:
                if(self.__mechanic_id==101 and self.__vehicle_type=="TW"):
                    vehicle_count_list[0]+1
                    return 1
                elif(self.__mechanic_id==102 and self.__vehicle_type=="FW"):
                    vehicle_count_list[0]+1
                    return 1
                elif(self.__mechanic_id==103 and self.__vehicle_type=="TW"):
                    vehicle_count_list[0]+1
                    return 1
                elif(self.__mechanic_id==104 and self.__vehicle_type=="FW"):
                    vehicle_count_list[0]+1
                    return 1
                elif(self.__mechanic_id==105 and self.__vehicle_type=="FW"):
                    vehicle_count_list[0]+1
                    return 1
        
class Mechanic(VehicleService):
    def __init__(self,mechanic_id,specialization,vehicle_count):
        self.__mechanic_id=mechanic_id
        self.__specialization =specialization
        self.__vehicle_count = vehicle_count
        super().__init__(mechanic_list)
    def get_mechanic_id(self):
        return self.__mechanic_id


    def get_specialization(self):
        return self.__specialization


    def get_vehicle_count(self):
        return self.__vehicle_count


    def set_mechanic_id(self, mechanic_id):
        self.__mechanic_id = mechanic_id


    def set_specialization(self, specialization):
        self.__specialization = specialization


    def set_vehicle_count(self, vehicle_count):
        self.__vehicle_count = vehicle_count


        
mechanic_list=[101,102,103,104,105]
specialization_list=['TW','FW','TW','FW','FW']
vehicle_count_list=[1,0,4,2,1]


m1=Mechanic(101,"TW",1)
m2=Mechanic(102,"FW",0)
m3=Mechanic(103,"TW",4)

try:   
    m4=Mechanic(104,"TW",2)   #false
    m5=Mechanic(105,"TW",1)   #false

except Exception:
    print("Exception")
    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        