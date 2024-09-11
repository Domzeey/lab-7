class Student: 
    
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.modules_list = []
    
    def print_student_info(self):
        print("Student name: %s" %self.name)
        print("Student ID: %s" %self.student_number)
        print("module/s undertaken by the studen:" )
        i = 0
        for c in self.modules_list:
                i+=1
                print("%d %s" %(i,c.print_module_info()))
        
    def enrol(self, module_running):
        self.modules_list.append(module_running)



class Module:  
    
    def __init__(self, module_title, module_credits, department):
        self.module_title = module_title
        self.credits = module_credits
        self.department = department
    
    def print_module_info(self):
        return "%s, Credits: %s, Department: %s" %(self.module_title, self.credits, self.department)
    
def main():
    student1 = Student("solo", 12345)
    student2 = Student("dom", 654321)
        
      
    module1 = Module("Mathematics", 5, "Math Department")
    module2 = Module("Physics", 4, "Physics Department")
    module3 = Module("History", 3, "History Department")

       
    student1.enrol(module1)
    student2.enrol(module2)
    student2.enrol(module3)


    student1.print_student_info()
    student2.print_student_info()
        
main()

