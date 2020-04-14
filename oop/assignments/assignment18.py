

class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity
        
    def get_item_id(self):
        return self.__item_id
    
    def get_description(self):
        return self.__description
    
    def get_price_per_quantity(self):
        return self.__price_per_quantity
    
class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id=0
        self.__bill_amount=0

    def get_bill_id(self):
        return self.__bill_id


    def get_bill_amount(self):
        return self.__bill_amount
    
    def generate_bill_amount(self,item_quantity,items):
        if not self.__bill_amount:
            for key,value in item_quantity.items():
                for item in items:
                    if item.get_item_id()==key.upper():
                        self.__bill_amount += value*item.get_price_per_quantity()
                        continue
            
            if(self.__bill_amount>0):
                self.__bill_id = str("B")+str(Bill.counter+1)
                Bill.counter+=1
        
        
class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None

    def get_customer_name(self):
        return self.__customer_name


    def get_payment_status(self):
        return self.__payment_status

    def pays_bill(self,bill):
        pass

    
        
        
        
        
        
        

