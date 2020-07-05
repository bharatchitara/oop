class Rider:
    def __init__(self,trained_status,experience):
        self.__experience = 6
        self.__trained_status = True
    
    
    def rides_vehicle(self):
        if(self.__experience>=1 and self.__trained_status==1):
            return True
        else:
            return False
        

class CycleRider(Rider):
    
    def rides_blindfolded(self):
        print("rides blindfolded")
        

class BikeRider(Rider):
    
    def __init__(self,trained_status,experience):
        super().__init__(trained_status, experience)
        self.__race_license = None
    
        
        
    def rides_in_dome(self):
        print("rides in dome")



