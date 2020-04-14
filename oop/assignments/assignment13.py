class Classroom:
    classroom_list=[12,13,14,15,16]
    
    @staticmethod
    def search_classroom(class_room):
        if(class_room in Classroom.classroom_list):
            return "Found"
        else:
            return -1
        
print(Classroom.search_classroom(12))