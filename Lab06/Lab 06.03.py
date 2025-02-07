class Student:
    def __init__(self,std_id:int,name,gpa:float):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa
    
    def print_detail(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")
    
    def getterID(self):
        return self.__std_id
    
    def getterName(self):
        return self.__name
    
    def getterGpa(self):
        return self.__gpa
    
def binary_search(data,name):
    start, end = 0, len(data) - 1
    time = 0
    while start <= end:
        time += 1
        mid = (start + end) // 2
        mid_name = data[mid].getterName()
        
        if mid_name == name:
            print("Found",name,"at index",mid)
            data[mid].print_detail()
            print("Comparisons times:", time)
            return
        
        if mid_name > name:
            end = mid - 1 
        
        elif mid_name < name:
            start = mid + 1
    print(name,"does not exists.")
    print("Comparisons times:",time)

def main():
    text_in = input()
    name = input()
    student_data = []
    import json
    students_list = json.loads(text_in)
    for student in students_list:
        std = Student(student["id"], student["name"], student["gpa"])
        student_data.append(std)
    binary_search(student_data,name)
main()