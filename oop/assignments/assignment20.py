class Applicant:
    __application_dict={'a':4,'b':2}
    __applicant_id_count=1000
    
    def __init__(self,applicant_name):
        self.__applicant_name=applicant_name
        self.__applicant_id=None
        self.__job_band=None

    @staticmethod
    def get_application_dict(self):
        return Applicant.__application_dict


    def get_applicant_name(self):
        return self.__applicant_name


    def get_applicant_id(self):
        return self.__applicant_id


    def get_job_band(self):
        return self.__job_band
    
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
        #print(self.__applicant_id)
    
    def apply_for_job(self,job_band):
        
        for key,value in Applicant.__application_dict.items():
            if(key==job_band.lower()):
                if(value>5):
                    return -1
            else:
                Applicant.__application_dict[key]+=1
                self.generate_applicant_id()
                self.__job_band=job_band
               # print(Applicant.__application_dict)
                    
    
    
    
    
    