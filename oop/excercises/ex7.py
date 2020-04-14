#from builtins import True
class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None

    def get_passenger_name(self):
        return self.__passenger_name


    def get_source(self):
        return self.__source


    def get_destination(self):
        return self.__destination


    def get_ticket_id(self):
        return self.__ticket_id

        
    
    
    def validate_source_destination(self):
        
        if(self.__source.lower()=="delhi"):
            if(self.__destination.lower()== "mumbai" or self.__destination.lower() == "chennai" or self.__destination.lower() == "pune" or self.__destination.lower() == "kolkata"):
                return True
            else:
                return False
        else:
            return False
    
    def generate_ticket(self):
        if(self.validate_source_destination()):
            
            self.__ticket_id = str(self.__source[0])+str(self.__destination[0])+str(0)+str(Ticket.counter)
            print(self.__ticket_id)
            
            print(self.__passenger_name)
            print(self.__source)
            print(self.__destination)
            
            
        else:
            self.__ticket_id=None    
            
t1=Ticket("bharat","Delhi","Mumbai")
t1.generate_ticket()
t1.get_destination()