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
        
class ProbHash:
    def __init__(self,size:int):
        self.hash_table = [None]*size
        self.size = size

    def hash(self,key:int):
        return key % self.size
    
    def rehash(self,hkey:int):
        return (hkey+1) % self.size
    
    def insert_data(self,student):
        index = self.hash(student.getterID())
        original_index = index
        if self.hash_table[index] is None:
            self.hash_table[index] = student
            print("Insert",student.getterID(),"at index",index)
            return
            
        while self.hash_table[index] is not None:
            index = self.rehash(index)
            if index == original_index:
                print("The list is full.",student.getterID(),"could not be inserted.")
                return
        self.hash_table[index] = student
        print("Insert",student.getterID(),"at index",index)
    
    def search_data(self,std_id):
        for i in range(self.size):
            if self.hash_table[i] is not None and self.hash_table[i].getterID() == std_id:
                print("Found",std_id,"at index",i)
                return self.hash_table[i]
            
        print(std_id,"does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()