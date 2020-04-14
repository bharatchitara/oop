flowers=['Orchid','Rose','Jasmine']
levels=[15,25,40]

class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None

    def get_flower_name(self):
        return self.__flower_name


    def get_price_per_kg(self):
        return self.__price_per_kg


    def get_stock_available(self):
        return self.__stock_available


    def set_flower_name(self, flower_name):
        
        self.__flower_name = flower_name
        


    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg


    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available

 
    def validate_flower(self):
        
        if(self.__flower_name in flowers ):
            return True
        else:
            return False
        
    def validate_stock(self,required_quantity):
        self.__flower_name.lower()
        if self.__stock_available>=required_quantity:
            return True
        else:
            return False
        
    def sell_flower(self,required_quantity):
        self.__flower_name.lower()
        if(self.validate_flower() and self.validate_stock(required_quantity)):
            self.__stock_available -= required_quantity
            
    def check_level(self):
        self.__flower_name.lower()
        
        if self.validate_flower():
            flower_level=levels[flowers.index(self.__flower_name)]
            if self.__stock_available < flower_level:
                return True
        return False
    
f1=Flower()
f1.set_flower_name("Orchid")
f1.set_price_per_kg(200)
f1.set_stock_available(15)
print(f1.check_level())
             
            