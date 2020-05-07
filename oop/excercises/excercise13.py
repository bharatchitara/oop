from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass= ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name
        self.__consumer_number= DirectToHomeService.__counter
        DirectToHomeService.__counter+=1

    def get_consumer_name(self):
        return self.__consumer_name


    def get_consumer_number(self):
        return self.__consumer_number
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass
    
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
        super().__init__(consumer_name)
    
    
    def get_base_pack_name(self):
        return self.__base_pack_name


    def get_subscription_period(self):
        return self.__subscription_period

    def validate_base_pack_name(self):
        if(self.__base_pack_name.title()=="Silver" or self.__base_pack_name.title()== "Gold" or self.__base_pack_name.title()=="Platinum" ):
            return 1
        else:
            self.__base_pack_name= "Silver"
            return "Base package name is incorrect, set to Silver"
        
    
    def calculate_monthly_rent(self):
        monthly_rent=0
        total_monthly_rent=0
    
        if(self.__subscription_period>=1 and self.__subscription_period<=24):
            if(self.__subscription_period>12):
                
                if(self.__base_pack_name.title() == "Silver"):
                    monthly_rent=350
                    
                    total_monthly_rent = ((monthly_rent* self.__subscription_period)- monthly_rent)/self.__subscription_period
            
                elif(self.__base_pack_name.title() == "Gold"):
                    monthly_rent=440
                    total_monthly_rent = ((monthly_rent* self.__subscription_period)- monthly_rent)/self.__subscription_period
            
                elif(self.__base_pack_name.title() == "Platinum"):
                    monthly_rent=560
                    total_monthly_rent = ((monthly_rent* self.__subscription_period)- monthly_rent)/self.__subscription_period
                    
                return total_monthly_rent
        
            else:
                if(self.__base_pack_name.title() == "Silver"):
                    monthly_rent=350
                    
                    total_monthly_rent = ((monthly_rent* self.__subscription_period))/self.__subscription_period
                    #return total_monthly_rent
                
                elif(self.__base_pack_name.title() == "Gold"):
                    monthly_rent=440
                    total_monthly_rent = ((monthly_rent* self.__subscription_period))/self.__subscription_period
            
                elif(self.__base_pack_name.title() == "Platinum"):
                    monthly_rent=560
                    total_monthly_rent = ((monthly_rent* self.__subscription_period))/self.__subscription_period
            
                return total_monthly_rent
                            
        else:
            return -1
        
c1=BasePackage("bharat","gold",13)
print(c1.calculate_monthly_rent())    
print(c1.validate_base_pack_name())    
    
    
    