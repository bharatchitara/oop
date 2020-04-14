class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=None

    def get_bill_id(self):
        return self.__bill_id


    def get_patient_name(self):
        return self.__patient_name


    def get_bill_amount(self):
        return self.__bill_amount

    
    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        x=0
        y=0
        for i in range(0,len(price_list)):
            x += (quantity_list[i]*price_list[i])
        self.__bill_amount = consultation_fees+x
        
        return self.__bill_amount

b1=Bill(101,"bharat")
print(b1.calculate_bill_amount(100, [1,2,3], [100,200,300]))        