# CMS

import pickle
# BLL
class Customer:
  cus_list=[]
  def __init__(self):
    self.id=0
    self.name=0
    self.age=0
    self.mob=0

  def addCustomer(self):
    Customer.cus_list.append(self)

  def searchCustomer(self):
    for e in Customer.cus_list:
      if (e.id==self.id):
        self.name=e.name
        self.age=e.age
        self.mob=e.mob
        return
  
  def deleteCustomer(self):
    for e in Customer.cus_list:
      if e.id==self.id:
        Customer.cus_list.remove(e)
        return
  def modifyCustomer(self):
    for e in Customer.cus_list:
      if e.id==self.id:
        e.name=self.name
        e.age=self.age
        e.mob=self.mob
        return

  @staticmethod
  def save():
    f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/Project/Cust_list.txt','wb')
    pickle.dump(Customer.cus_list,f)
    f.close()
  
  @staticmethod
  def load():
      f=open('C:/Users/nitil/Downloads/Telegram Desktop/Python/Project/Cust_list.txt','rb')
      Customer.cus_list=pickle.load(f)
      f.close()
# PL
if (__name__=='__main__'):
  print('Welcome to CMS')

  def showCustomer(cus):
    print('Cust ID:',cus.id,'Cust Name:',cus.name,'Cust Age:',cus.age,'Cust Mob:',cus.mob)

  while(1):
    ch=input('Enter Choice: 1.add 2.search 3.delete 4.modify 5.display all 6.save 7.load 8.exit: ')
    if ch=='1':
      cus=Customer()
      cus.id=input('Enter Customer ID: ')
      cus.name=input('Enter Customer Name: ')
      cus.age=input('Enter Customer Age: ')
      cus.mob=input('Enter Customer Mobile No. : ')
      cus.addCustomer()
      print('Customer Added Successfully')
    
    elif ch=='2':
      cus=Customer()
      cus.id=input('Enter Customer ID to Search: ')
      cus.searchCustomer()
      showCustomer(cus)

    elif ch=='3':
      cus=Customer()
      cus.id=input('Enter Customer ID to Delete: ')
      cus.deleteCustomer()
      print('Customer Deleted Successfully')
    
    elif ch=='4':
      cus=Customer()
      cus.id=input('Enter Customer ID to Modify: ')
      cus.name=input('Enter Customer Name to Modify: ')
      cus.age=input('Enter Customer Age to Modify: ')
      cus.mob=input('Enter Customer Mobile No. to Modify: ')
      cus.modifyCustomer()
      print('Customer Modified Successfully')

    elif ch=='5':
      for e in Customer.cus_list:
        showCustomer(e)
    
    elif ch=='6':
      Customer.save()
      print('Customer Saved Successfully')
    
    elif ch=='7':
      Customer.load()
      print('Customer Loaded Successfully')
    
    elif ch=='8':
      print('Thank You for Using CMS')
      break

    else:
      print("Incorrect Choice")