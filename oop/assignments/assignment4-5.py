


class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
        self.flag=False
    
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id=vehicle_id
     
    def set_vehicle_type(self, vehicle_type):
        if vehicle_type=="TwoWheeler" or vehicle_type=="FourWheeler":
            self.__vehicle_type=vehicle_type
        else:
            print("Invalid vehicle Details!!")
     
    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost=vehicle_cost
     
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
 
    def get_vehicle_id(self):
        return self.__vehicle_id
     
    def get_vehicle_type(self):
        return self.__vehicle_type
     
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    
    def get_premium_amount(self):
        return self.__premium_amount
     
    def calculate_premium(self):
        if self.__vehicle_type=="TwoWheeler" or self.__vehicle_type=="FourWheeler":
            if self.__vehicle_type=="TwoWheeler":
                self.__premium_amount=self.__vehicle_cost*0.02
            else:
                self._premium_amount=self.__vehicle_cost*0.06
            self.flag=True
        else:
            print("vehicle Type not Matched")
        
        return self.__premium_amount
    
    def display_vehicle_details(self):
        if self.flag==True:
#             print("=================================")
#             print("---------vehicle Details---------")
#             print("vehicle Id :",self.__vehicle_id)
#             print("vehicle Type :",self.__vehicle_type) 
#             print("Vehicl Cost :",self.__vehicle_cost)
            print(self.__premium_amount)       
           # print("=================================")
        else:
            print("vehicle Details Can't fatched !!")
vecl=Vehicle()
vecl.set_vehicle_id("Vcl100")
vecl.set_vehicle_type("TwoWheeler")
vecl.set_vehicle_cost(50000)
vecl.calculate_premium()
vecl.display_vehicle_details()




