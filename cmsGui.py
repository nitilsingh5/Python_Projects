from cms import *
from tkinter import *
from tkinter import messagebox
#BLL
def addCust():
  cus=Customer()
  cus.id=var_id.get()
  cus.name=var_name.get()
  cus.age=var_age.get()
  cus.mob=var_mob.get()
  cus.addCustomer()
  messagebox.showinfo(message='Customer Added',title='CMS')
  var_id.set('')
  var_name.set('')
  var_age.set('')
  var_mob.set('')

def searchCust():
  cus=Customer()
  cus.id=var_id.get()
  cus.searchCustomer()
  var_name.set(cus.name)
  var_age.set(cus.age)
  var_mob.set(cus.mob)

def refresh():
  var_id.set('')
  var_name.set('')
  var_age.set('')
  var_mob.set('')

def deleteCust():
  cus=Customer()
  cus.id=var_id.get()
  cus.deleteCustomer()
  messagebox.showinfo(message='Customer Deleted',title='CMS')
  var_id.set('')

def modifyCust():
  cus=Customer()
  cus.id=var_id.get()
  cus.name=var_name.get()
  cus.age=var_age.get()
  cus.mob=var_mob.get()
  cus.modifyCustomer()
  messagebox.showinfo(message='Customer Added',title='CMS')
  var_id.set('')
  var_name.set('')
  var_age.set('')
  var_mob.set('')


def displayAllCust():
  root_all=Tk()
  root_all.title('All Customer Details')
  lb_id=Label(root_all,text='CUST ID',font=1,bg='orange',width=10,height=3)
  lb_id.grid(row=0,column=0)
  lb_name=Label(root_all,text='CUST NAME',font=1,bg='orange',width=10,height=3)
  lb_name.grid(row=0,column=1)
  lb_age=Label(root_all,text='CUST AGE',font=1,bg='orange',width=10,height=3)
  lb_age.grid(row=0,column=2)
  lb_mob=Label(root_all,text='CUST MOB',font=1,bg='orange',width=10,height=3)
  lb_mob.grid(row=0,column=3)

  i=0
  for e in Customer.cus_list:
    i+=1
    id=Label(root_all,text=e.id,font=1,bg='Yellow',width=10,height=2)
    id.grid(row=i,column=0)
    name=Label(root_all,text=e.name,font=1,bg='Yellow',width=10,height=2)
    name.grid(row=i,column=1)
    age=Label(root_all,text=e.age,font=1,bg='Yellow',width=10,height=2)
    age.grid(row=i,column=2)
    mob=Label(root_all,text=e.mob,font=1,bg='Yellow',width=10,height=2)
    mob.grid(row=i,column=3)


def saveCust():
  Customer.save()
  messagebox.showinfo(message='Customers Saved',title='CMS')

def loadCust():
  Customer.load()
  messagebox.showinfo(message='Customers Loaded',title='CMS')


#PL
root=Tk()
root.title('Nitil Customer Management System')
root.config(bg='orange')

lbl_id=Label(root,text='Cust ID',font=1,bg='orange')
lbl_id.grid(row=0,column=0)
lbl_name=Label(root,text='Cust Name',font=1,bg='orange')
lbl_name.grid(row=1,column=0)
lbl_age=Label(root,text='Cust Age',font=1,bg='orange')
lbl_age.grid(row=2,column=0)
lbl_mob=Label(root,text='Cust Mob',font=1,bg='orange')
lbl_mob.grid(row=3,column=0)

var_id=StringVar()
ent_id=Entry(root,textvariable=var_id,font=1)
ent_id.grid(row=0,column=1)
var_name=StringVar()
ent_name=Entry(root,textvariable=var_name,font=1)
ent_name.grid(row=1,column=1)
var_age=StringVar()
ent_age=Entry(root,textvariable=var_age,font=1)
ent_age.grid(row=2,column=1)
var_mob=StringVar()
ent_mob=Entry(root,textvariable=var_mob,font=1)
ent_mob.grid(row=3,column=1)

btn_add_cust=Button(root,text='ADD CUST',font=1,command=addCust,width=15,height=3,bg='yellow')
btn_add_cust.grid(row=4,column=0)
btn_search_cust=Button(root,text='SEARCH CUST',font=1,command=searchCust,width=15,height=3,bg='yellow')
btn_search_cust.grid(row=4,column=1)
btn_delete_cust=Button(root,text='DELETE CUST',font=1,command=deleteCust,width=15,height=3,bg='yellow')
btn_delete_cust.grid(row=4,column=2)
btn_modify_cust=Button(root,text='MODIFY CUST',font=1,command=modifyCust,width=15,height=3,bg='yellow')
btn_modify_cust.grid(row=5,column=0)
btn_display_all=Button(root,text='Display ALL',font=1,command=displayAllCust,width=15,height=3,bg='yellow')
btn_display_all.grid(row=5,column=1)
btn_save_cust=Button(root,text='Save All CUST',font=1,command=saveCust,width=15,height=3,bg='yellow')
btn_save_cust.grid(row=5,column=2)
btn_load_cust=Button(root,text='LOAD All CUST',font=1,command=loadCust,width=15,height=3,bg='yellow')
btn_load_cust.grid(row=6,column=0)
btn_refresh=Button(root,text='Refresh',font=1,command=refresh,width=15,height=3,bg='yellow')
btn_refresh.grid(row=6,column=1)

root.mainloop()
