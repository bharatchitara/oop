class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.__price=price
        self.__item_type=item_type
        self.__item_id= item_type[0].upper()+str(Apparel.counter+1)
        Apparel.counter+=1

    def get_price(self):
        return self.__price


    def get_item_type(self):
        return self.__item_type


    def get_item_id(self):
        
        return self.__item_id


    def set_price(self, price):
        self.__price = price

    def calculate_price(self):
        st=5
        self.__price += (self.__price * (st/100))
        
    
class Cotton(Apparel):
    def __init__(self,price,discount):
        
        super().__init__(price,"Cotton")
        self.__discount=discount
        self.__price = 0
        
    def get_discount(self):
        return self.__discount


    def calculate_price(self):
        vat=5
        self.__price-=(self.__price*self.__discount)
        self.__price= (self.__price * (1.05))

class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price, "Silk")
        self.__points=0
        self.__price=0
        
    def get_points(self):
        return self.__points
        
    def calculate_price(self):
        vat=10
        if(self.__price>10000):
            self.__points+=10
        elif(self.__price<=10000):
            self.__points+=3
        
        self.__price = (self.__price*1.10)
        return self.__points


app=Apparel(3000,"Silk")
cott=Cotton(1500,5)
si=Silk(app)
cott.calculate_price()
si.calculate_price()    