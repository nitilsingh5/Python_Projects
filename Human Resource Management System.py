#Human Resource Management System

import pickle
#BLL
class Employee:
    emp_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=self.mob=0
    def addEmployee(self):
        Employee.emp_list.append(self)
    def searchEmployee(self):
        for e in Employee.emp_list:
            if e.id==self.id:
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                return
    def deleteEmployee(self):
        for e in Employee.emp_list:
            if e.id==self.id:
                Employee.emp_list.remove(e)
                return
    def modifyEmployee(self):
        for e in Employee.emp_list:
            if e.id==self.id:
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return
    @staticmethod
    def saveEmployee():
        f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/emp_list.txt','wb')
        pickle.dump(Employee.emp_list,f)
        f.close()
        return
    @staticmethod
    def loadEmployee():
        f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/emp_list.txt','rb')
        Employee.emp_list=pickle.load(f)
        f.close()
        return

class Trainer(Employee):
    trn_list=[]
    def __init__(self):
        self.course=0
        super().__init__()
    def addTrainer(self):
        Trainer.trn_list.append(self)
    def searchTrainer(self):
        for e in Trainer.trn_list:
            if e.id==self.id:
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.course=e.course
                return
    def deleteTrainer(self):
        for e in Trainer.trn_list:
            if e.id==self.id:
                Trainer.trn_list.remove(e)
                return
    def modifyTrainer(self):
        for e in Trainer.trn_list:
            if e.id==self.id:
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.course=self.course
                return
    @staticmethod
    def saveTrainer():
        f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/trn_list.txt','wb')
        pickle.dump(Trainer.trn_list,f)
        f.close()
        return
    @staticmethod
    def loadTrainer():
        f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/trn_list.txt','rb')
        Trainer.trn_list=pickle.load(f)
        f.close()
        return

class Manager(Employee):
    mng_list=[]
    def __init__(self):
        self.branch=0
        super().__init__()
    def addManager(self):
        Manager.mng_list.append(self)
    def searchManager(self):
        for e in Manager.mng_list:
            if e.id==self.id:
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.branch=e.branch
                return
    def deleteManager(self):
        for e in Manager.mng_list:
            if e.id==self.id:
                Manager.mng_list.remove(e)
                return
    def modifyManager(self):
        for e in Manager.mng_list:
            if e.id==self.id:
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.branch=self.branch
                return
    @staticmethod
    def saveManager():
        f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/mng_list.txt','wb')
        pickle.dump(Manager.mng_list,f)
        f.close()
        return
    @staticmethod
    def loadManager():
        f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/mng_list.txt','rb')
        Manager.mng_list=pickle.load(f)
        f.close()
        return
#PL
print('Welcome to HRMS')


def getMob():
    while(1):
        mob=input('Enter Employee Mobile: ')
        if mob.isdecimal():
                if (len(mob)==10):
                        return mob
                else:
                        print('Please Enter mobile no. in 10 digits')
        else:
                print('Only Whole number')

def showEmployee(emp):
    print('Emp Id:',emp.id,'Emp Name:',emp.name,'Emp Age:',emp.age,'Emp Mob:',emp.mob)
def showTrainer(trn):
    print('Trn Id:',trn.id,'Trn Name:',trn.name,'Trn Age:',trn.age,'Trn Mob:',trn.mob,'Trn Course:',trn.course)
def showManager(mng):
    print('Mng Id:',mng.id,'Mng Name:',mng.name,'Mng Age:',mng.age,'Mng Mob:',mng.mob,'Mng Branch:',mng.branch)

while(1):
    ch=input('Enter Choice: 1.add employee 2.add trainer 3.add manager 4. exit: ')
    if ch=='1':
        while(1):
            ch=input('Enter Choice: 1.add 2.search 3.delete 4.modify 5.display all 6.save 7.load 8. back to main menu: ')
            if ch=='1':
            # Add Employee
                emp=Employee()
                emp.id=input('Enter Employee ID: ')
                emp.name=input('Enter Employee Name: ')
                emp.age=input('Enter Employee Age: ')
                emp.mob=getMob()
                emp.addEmployee()
                print('Employee Added')
            elif ch=='2':
            # Search Employee
                emp=Employee()
                emp.id=input('Enter Employee id To search: ')
                emp.searchEmployee()
                showEmployee(emp)
            elif ch=='3':
            # Delete Employee
                emp=Employee()
                emp.id=input('Enter Employee id to delete ')
                emp.deleteEmployee()
                print('Employee Deleted')
            elif ch=='4':
                # Modify Employee
                emp=Employee()
                emp.id=input('Enter Employee id to modify ')
                emp.name=input('Enter Employee Name to modify: ')
                emp.age=input('Enter Employee Age to modify: ')
                emp.mob=getMob()
                emp.modifyEmployee()
                print('Employee Modified')
            elif ch=='5':
            # Display All Employee
                for e in Employee.emp_list:
                    showEmployee(e)
            elif ch=='6':
            # Save Employee
                Employee.saveEmployee()
                print('Saved')
            elif ch=='7':
            # Load Employee
                Employee.loadEmployee()
                print('Loaded')
            elif ch=='8':
            # Exit Employee
                break
            else:
                print('Incorrect Choice')
    elif ch=='2':
        while(1):
            ch=input('Enter Choice: 1.add 2.search 3.delete 4.modify 5.display all 6.save 7.load 8. back to main menu: ')
            if ch=='1':
                # Add Trainer
                trn=Trainer()
                trn.id=input('Enter Trainer ID: ')
                trn.name=input('Enter Trainer Name: ')
                trn.age=input('Enter Trainer Age: ')
                trn.mob=getMob()
                trn.course=input('Enter Trainer Course: ')
                trn.addTrainer()
                print('Trainer Added')
            elif ch=='2':
                # Search Trainer
                trn=Trainer()
                trn.id=input('Enter Trainer id To search: ')
                trn.searchTrainer()
                showTrainer(trn)
            elif ch=='3':
                # Delete Trainer
                trn=Trainer()
                trn.id=input('Enter Trainer id to delete ')
                trn.deleteTrainer()
                print('Trainer Deleted')
            elif ch=='4':
                # Modify Trainer
                trn=Trainer()
                trn.id=input('Enter Trainer id to modify ')
                trn.name=input('Enter Trainer Name to modify: ')
                trn.age=input('Enter Trainer Age to modify: ')
                trn.mob=getMob()
                trn.course=input('Enter Trainer Course to modify: ')
                trn.modifyTrainer()
                print('Trainer Modified')
            elif ch=='5':
                # Display All Trainer
                for e in Trainer.trn_list:
                    showTrainer(e)
            elif ch=='6':
                # Save Trainer
                Trainer.saveTrainer()
                print('Saved')
            elif ch=='7':
                # Load Trainer
                Trainer.loadTrainer()
                print('Loaded')
            elif ch=='8':
                # Exit Trainer
                break
            else:
                print('Incorrect Choice')
    elif ch=='3':
        while(1):
            ch=input('Enter Choice: 1.add 2.search 3.delete 4.modify 5.display all 6.save 7.load 8. back to main menu: ')
            if ch=='1':
                # Add Manager
                mng=Manager()
                mng.id=input('Enter Manager ID: ')
                mng.name=input('Enter Manager Name: ')
                mng.age=input('Enter Manager Age: ')
                mng.mob=getMob()
                mng.branch=input('Enter Manager Branch: ')
                mng.addManager()
                print('Manager Added')
            elif ch=='2':
                # Search Manager
                mng=Manager()
                mng.id=input('Enter Manager id To search: ')
                mng.searchManager()
                showManager(mng)
            elif ch=='3':
                # Delete Manager
                mng=Manager()
                mng.id=input('Enter Manager id to delete ')
                mng.deleteManager()
                print('Manager Deleted')
            elif ch=='4':
                # Modify Manager
                mng=Manager()
                mng.id=input('Enter Manager id to modify ')
                mng.name=input('Enter Manager Name to modify: ')
                mng.age=input('Enter Manger Age to modify: ')
                mng.mob=getMob()
                mng.branch=input('Enter Manger Branch to modify: ')
                mng.modifyManager()
                print('Manager Modified')
            elif ch=='5':
                # Display All Manager
                for e in Manager.mng_list:
                    showManager(e)
            elif ch=='6':
                # Save Manger
                Manager.saveManager()
                print('Saved')
            elif ch=='7':
                # Load Manager
                Manager.loadManager()
                print('Loaded')
            elif ch=='8':
                # Exit Manager
                break
            else:
                print('Incorrect Choice')
            
    elif ch=='4':
        print('Thnks For Using HRMS')
        break
    else:
        print('Incorrect Choice')