class FruitInfo:
    __fruit_name_list=['Apple','Guava','Orange','Grape','Sweet lime']
    __fruit_price_list=[200,80,70,110,60]
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    
    @staticmethod
    def get_fruit_price(fruit_name):
        if(fruit_name.title() not in FruitInfo.__fruit_name_list):
            return -1
        else:
            return FruitInfo.__fruit_price_list[FruitInfo.__fruit_name_list.index(fruit_name.title())]
    

class Purchase:
    __counter=101
    def __init__(self,customer,fruit_name,quantity):
        self.__customer=customer
        self.__fruit_name=fruit_name
        self.__quantity=quantity
        self.__purchase_id=0

    def get_customer(self):
        return self.__customer


    def get_quantity(self):
        return self.__quantity


    def get_purchase_id(self):
        return self.__purchase_id

    def calculate_price(self):
        each_fruit_price=FruitInfo.get_fruit_price(self.__fruit_name)
        if(each_fruit_price>0):
            self.__purchase_id = str("P")+ str(Purchase.__counter)
            Purchase.__counter+=1
            price=each_fruit_price*self.__quantity
            if(each_fruit_price== max(FruitInfo.get_fruit_price_list()) and self.__quantity>=1):
               price = (price * 0.98)
            if(each_fruit_price== min(FruitInfo.get_fruit_price_list()) and self.__quantity>=5):
                 price = (price * 0.95) 
            if(Customer.get_cust_type(self.__customer)=="wholesale"):
                price = (price * 0.90)
            return price
        else:
            return -1
            
            

class Customer:
    def __init__(self,customer_name,cust_type):
        self.__customer_name=customer_name
        self.__cust_type=cust_type

    def get_customer_name(self):
        return self.__customer_name


    def get_cust_type(self):
        return self.__cust_type


c=Customer("Tom", "wholesale")
p=Purchase(c,"Orange", 5)
print(p.calculate_price())