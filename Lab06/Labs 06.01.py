class Student:
    def __init__(self,name,std_id:int,gpa:float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    
    def print_detail(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")
    
def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()

main(input())