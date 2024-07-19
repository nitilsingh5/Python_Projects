# Human Resource Management System

#BLL
class Employee:
    emp_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addEmployee(self):
        Employee.emp_list.append(self)
    def searchemployee(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                return
    def deleteEmployee(self):
          for e in Employee.emp_list:
            if (e.id==self.id):
                Employee.emp_list.remove(e)
                return
          Employee.emp_list.pop()
    def modifyEmployee(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return
class Manager(Employee):
    def __init__(self):
        self.branch=0
        super().__init__()
    def addManager(self):
        Employee.emp_list.append(self)
    def searchManager(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.branch=e.branch
                return
    def deleteManager(self):
          for e in Employee.emp_list:
            if (e.id==self.id):
                Employee.emp_list.remove(e)
                return
          Employee.emp_list.pop()
    def modifyManager(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.branch=self.branch
                return  
class Trainer(Employee):
    def __init__(self):
        self.course=0
        super().__init__()
    def addTrainer(self):
        Employee.emp_list.append(self)
    def searchTrainer(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.course=e.course
                return
    def deleteTrainer(self):
          for e in Employee.emp_list:
            if (e.id==self.id):
                Employee.emp_list.remove(e)
                return
          Employee.emp_list.pop()
    def modifyTrainer(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.course=self.course
                return
class Director(Employee):
    def __init__(self):
        self.share=0
        super().__init__()
    def addDirector(self):
        Employee.emp_list.append(self)
    def searchDirector(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.share=e.share
                return
    def deleteDirector(self):
          for e in Employee.emp_list:
            if (e.id==self.id):
                Employee.emp_list.remove(e)
                return
          Employee.emp_list.pop()
    def modifyDirector(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.share=self.share
                return

#PL
print("Welcome To Nitil HRMS")
def showEmployee(emp):
    print("Emp ID: ",emp.id,"Emp Name: ",emp.name,"Emp Age: ",emp.age,"Emp Mob: ",emp.mob)
def showManager(mng):
    print("Mng ID: ",mng.id,"Mng Name: ",mng.name,"Mng Age: ",mng.age,"mng Mob: ",mng.mob,"Mng Branch: ",mng.branch)
def showTrainer(trn):
    print("Trn ID: ",trn.id,"Trn Name: ",trn.name,"Trn Age: ",trn.age,"Trn Mob: ",trn.mob,"Trn Course: ",trn.course)
def showDirector(dir):
    print("Dir ID: ",dir.id,"Dir Name: ",dir.name,"Dir Age: ",dir.age,"Dir Mob: ",dir.mob,"Dir Share: ",dir.share)
def getMob():
    while(1):
        mob=input("Enter Mob No:")
        if(mob.isdecimal()):
            if(len(mob)==10):
                return mob
            else:
                print("Enter Mob No of 10 Digits Only")
        else:
            print("Enter mob nos with digits only")

while(1):
    ch = input("Enter choice: 1 for add employee, 2 Manager, 3 Trainer, 4 Diector,5 Exit: ")
    if (ch=="1"):
        while(1):
            ch = input("Enter Choice: a add Employee, b Search, c Delete, d Modify, e Displayall, f Exit: ")
                #Add Employee
            if (ch=="a"):
                emp=Employee()
                emp.id=input("Enter Employee ID : ")
                emp.name=input("Enter Employee Name : ")
                emp.age=input("Enter Employee Age : ")
                emp.mob=getMob()
                emp.addEmployee()
            
            #Search Employee
            elif (ch=="b"):
                emp=Employee()
                emp.id=input("Enter Employee ID to Seach: ")
                emp.searchemployee()
                showEmployee(emp)
            
            #Delete Employee
            elif (ch=="c"):
                emp=Employee()
                emp.id=input("Enter Employee ID to Delete: ")
                emp.deleteEmployee()
                showEmployee(emp)
            
            #Modify Employee
            elif (ch=="d"):
                emp=Employee()
                emp.id=input("Enter Employee  ID : ")
                emp.name=input("Enter Updated Employee Name : ")
                emp.age=input("Enter Updated Employee Age : ")
                emp.mob=getMob()
                emp.modifyEmployee()
                showEmployee(emp)
        
            #Display All Employee
            elif (ch=="e"):
                for i in Employee.emp_list:
                    showEmployee(i)
            
            #Exit
            elif (ch=="f"):
                print("Thanks")
                break
            else:
                print("Invalid Choice")    
        
    elif (ch=="2"):
        while(1):
            ch = input("Enter Choice: a add Manager, b Search, c Delete, d Modify, e Displayall, f Exit: ")
                #Add Manager
            if (ch=="a"):
                mng=Manager()
                mng.id=input("Enter Manager ID : ")
                mng.name=input("Enter Manager Name : ")
                mng.age=input("Enter Manager Age : ")
                mng.mob=getMob()
                mng.branch=input("Enter Branch Name : ")
                mng.addManager()
            
            #Search Manager
            elif (ch=="b"):
                mng=Manager()
                mng.id=input("Enter Manager ID to Seach: ")
                mng.searchManager()
                showManager(mng)
            
            #Delete Manager
            elif (ch=="c"):
                mng=Manager()
                mng.id=input("Enter Manager ID to Delete: ")
                mng.deleteManager()
                showManager(mng)
            
            #Modify Manager
            elif (ch=="d"):
                mng=Manager()
                mng.id=input("Enter Manager  ID : ")
                mng.name=input("Enter Updated Manager Name : ")
                mng.age=input("Enter Updated Manager Age : ")
                mng.mob=getMob()
                mng.branch=input("Enter Updated Branch Name : ")
                mng.modifyManager()
                showManager(mng)
        
            #Display All Manager
            elif (ch=="e"):
                for i in Employee.emp_list:
                    showManager(i)
            
            #Exit
            elif (ch=="f"):
                print("Thanks")
                break
            else:
                print("Invalid Choice")    

    elif (ch=="3"):
        while(1):
            ch = input("Enter Choice: a add Trainer, b Search, c Delete, d Modify, e Displayall, f Exit: ")
                #Add Trainer
            if (ch=="a"):
                trn=Trainer()
                trn.id=input("Enter Trainer ID : ")
                trn.name=input("Enter Trainer Name : ")
                trn.age=input("Enter Trainer Age : ")
                trn.mob=getMob()
                trn.course=input("Enter Course Name : ")
                trn.addTrainer()
            
            #Search Trainer
            elif (ch=="b"):
                trn=Trainer()
                trn.id=input("Enter Trainer ID to Seach: ")
                trn.searchTrainer()
                showTrainer(trn)
            
            #Delete Trainer
            elif (ch=="c"):
                trn=Trainer()
                trn.id=input("Enter Trainer ID to Delete: ")
                trn.deleteTrainer()
                showTrainer(trn)
            
            #Modify Trainer
            elif (ch=="d"):
                trn=Trainer()
                trn.id=input("Enter Trainer  ID : ")
                trn.name=input("Enter Updated Trainer Name : ")
                trn.age=input("Enter Updated Trainer Age : ")
                trn.mob=getMob()
                trn.course=input("Enter Updated Course Name : ")
                trn.modifyTrainer()
                showTrainer(trn)
        
            #Display All Trainer
            elif (ch=="e"):
                for i in Employee.emp_list:
                    showTrainer(i)
            
            #Exit
            elif (ch=="f"):
                print("Thanks")
                break
            else:
                print("Invalid Choice") 

    elif (ch=="4"):
        while(1):
            ch = input("Enter Choice: a add Director, b Search, c Delete, d Modify, e Displayall, f Exit: ")
                #Add Director
            if (ch=="a"):
                dir=Director()
                dir.id=input("Enter Director ID : ")
                dir.name=input("Enter Director Name : ")
                dir.age=input("Enter Director Age : ")
                dir.mob=getMob()
                dir.share=input("Enter Share : ")
                dir.addDirector()
            
            #Search Director
            elif (ch=="b"):
                dir=Director()
                dir.id=input("Enter Director ID to Seach: ")
                dir.searchDirector()
                showDirector(dir)
            
            #Delete Director
            elif (ch=="c"):
                dir=Director()
                dir.id=input("Enter Director ID to Delete: ")
                dir.deleteDirector()
                showDirector(dir)
            
            #Modify Director
            elif (ch=="d"):
                dir=Director()
                dir.id=input("Enter Director  ID : ")
                dir.name=input("Enter Updated Director Name : ")
                dir.age=input("Enter Updated Director Age : ")
                dir.mob=getMob()
                dir.share=input("Enter Updated Share : ")
                dir.modifyDirector()
                showDirector(dir)
        
            #Display All Director
            elif (ch=="e"):
                for i in Employee.emp_list:
                    showDirector(i)
            
            #Exit
            elif (ch=="f"):
                print("Thanks")
                break
            else:
                print("Invalid Choice")    
    elif (ch=="5"):
        print("Thanks")
        break
    else:
        print("Invalid Choice")