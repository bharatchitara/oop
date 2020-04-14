#from gi.overrides.Gdk import name
class Patient:
    def __init__(self,patient_id,patient_name,list_of_lab_test_ids):
        self.__patient_id = patient_id
        self.__patient_name=patient_name
        self.__list_of_lab_test_ids=list_of_lab_test_ids
        self.__lab_test_charge=None

    def get_patient_id(self):
        return self.__patient_id


    def get_patient_name(self):
        return self.__patient_name


    def get_list_of_lab_test_ids(self):
        return self.__list_of_lab_test_ids


    def get_lab_test_charge(self):
        return self.__lab_test_charge
    
    def calculate_lab_test_charge(self):
        self.__lab_test_charge=0
        for list in self.__list_of_lab_test_ids:
            if LabTestRepository.get_test_charge(list)>0:
                self.__lab_test_charge+=LabTestRepository.get_test_charge(list)
        #print(self.__lab_test_charge)
    
    
                
    
    
class LabTestRepository:
    __list_of_hospital_lab_test_ids=[101,102,103,104]
    __list_of_lab_test_charge=[50,200,170,90]
     
    @staticmethod
    def get_test_charge(lab_test_id):
        x=0
        
        if( lab_test_id in LabTestRepository.__list_of_hospital_lab_test_ids ):
            x= LabTestRepository.__list_of_hospital_lab_test_ids.index(lab_test_id)
            return LabTestRepository.__list_of_lab_test_charge[x]

        else:
            return -1

        

test_ids=[101,102]
patient1=Patient(12,"bharat",test_ids)
patient1.calculate_lab_test_charge()


a= LabTestRepository
print(a.get_test_charge(103))

        
        
