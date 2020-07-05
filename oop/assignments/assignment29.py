#from numpy.random._generator import np
from abc import abstractmethod,ABCMeta
class Customer(metaclass=ABCMeta):
    def __init__(self,customer_name):
        self.__customer_name = customer_name.title()
        self.bill_amount =0
        self.bill_id =None

    def get_customer_name(self):
        return self.__customer_name

    @abstractmethod    
    def calculate_bill_amount(self):
        pass

class OccasionalCustomer(Customer):
    __counter= 1000
      
    def __init__(self,customer_name,distance_in_kms):
        self.__distance_in_kms = distance_in_kms
        super().__init__(customer_name)
        self.bill_id = "O" +str(OccasionalCustomer.__counter+1)
        
    def validate_distance_in_kms(self):
        if(self.__distance_in_kms>=1 and self.__distance_in_kms<=5):
            return True
        else:
            return False
    
    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def calculate_bill_amount(self):
        cost_per_tiffin= 50
        if(self.validate_distance_in_kms()):
            if(self.__distance_in_kms>=1 and self.__distance_in_kms<=2):
                self.bill_amount =cost_per_tiffin + (self.__distance_in_kms*5)
            elif(self.__distance_in_kms>2 and self.__distance_in_kms<=5):
                self.bill_amount =cost_per_tiffin + (self.__distance_in_kms*7.5)
               
            return self.bill_amount
        else:
            self.bill_amount = -1
            
            return self.bill_amount
            
        
        
            
        #Customer.calculate_bill_amount(self) 
        
        
class RegularCustomer(Customer):
    __counter= 100
    
    def __init__(self,customer_name,no_of_tiffin):
        self.__no_of_tiffin = no_of_tiffin
        super().__init__(customer_name)
        self.bill_id = "R" +str(RegularCustomer.__counter+1)

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin

        
    def validate_no_of_tiffin(self):
        if(self.__no_of_tiffin>=1 and self.__no_of_tiffin<=7):
            return True
        else:
            return False
        
    
    
    def calculate_bill_amount(self):
      #  Customer.calculate_bill_amount(self)
        cost_per_tiffin = 50
        if(self.validate_no_of_tiffin()):
            self.bill_amount  = (self.__no_of_tiffin*cost_per_tiffin*7)
            return self.bill_amount
        else:
            self.bill_amount = -1
            return self.bill_amount
        
    
    
    
    
    
    
o=OccasionalCustomer("bharat", 5)
print(o.calculate_bill_amount())
    
    
    
    
    
    
      