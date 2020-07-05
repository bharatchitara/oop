 
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity
 
    def get_customer_name(self):
        return self.__customer_name
 
 
    def get_quantity(self):
        return self.__quantity
 
     
    def validate_quantity(self):
        if(self.__quantity>=1 and self.__quantity<=5):
            return True
        else:
            return False
         
     
class Pizzaservice():
     
    counter= 100
     
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer =customer
        self.__pizza_type = pizza_type
        self.__additional_topping  = additional_topping
        self.__service_id = None
        self.pizza_cost = 0
 
    def get_customer(self):
        return self.__customer
 
 
    def get_pizza_type(self):
        return self.__pizza_type
 
 
    def get_additional_topping(self):
        return self.__additional_topping
 
 
    def get_service_id(self):
        return self.__service_id
 
    def validate_pizza_type(self):
        if(self.__pizza_type.lower()=='small' or self.__pizza_type.lower()=='medium'):
            return True
        return False
     
     
    def calculate_pizza_cost(self):
        if(self.validate_pizza_type() and Customer.validate_quantity(self.__customer)):
            
            if(self.__additional_topping):
                if(self.__pizza_type.lower()=='small'):
                    self.__service_id = "S" +str(Pizzaservice.counter+1)
                    cost  = 150
                    additional =35
                    self.pizza_cost = (Customer.get_quantity(self.__customer))*(cost + additional)
                    
                elif(self.__pizza_type.lower()=='medium'):
                    self.__service_id = "M" +str(Pizzaservice.counter+1)
                    cost  = 200
                    additional =50
                    self.pizza_cost = (Customer.get_quantity(self.__customer))*(cost + additional)
    
            else:
                if(self.__pizza_type.lower()=='small'):
                    self.__service_id = "s" +str(Pizzaservice.counter+1)
                    cost  = 150
                    
                    self.pizza_cost = (Customer.get_quantity(self.__customer))*(cost)
                    
                elif(self.__pizza_type.lower()=='medium'):
                    self.__service_id = "m" +str(Pizzaservice.counter+1)
                    cost  = 200
                    
                    self.pizza_cost = (Customer.get_quantity(self.__customer))*(cost)
                
                
                    Pizzaservice.counter=+1
        else:
            self.pizza_cost = -1        
                         
class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms = distance_in_kms
        Pizzaservice.__init__(self, customer, pizza_type, additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!= -1:
                distance=1
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost += 5
                    if distance in range(6,11):
                        self.pizza_cost += 7
                    distance += 1
        else:
            self.pizza_cost = -1
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
c = Customer("Asha", 5)
d = Pizzaservice(c, "medium", True)
d.calculate_pizza_cost()

print(d.pizza_cost)
print(d.get_service_id())


