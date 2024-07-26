

from googletrans import Translator
from tkinter import *
def handler_hindi(e):
    src_data=var.get()
    res=t.translate(src_data,"Hi")
    data=res.text
    dest=StringVar()
    entr_dest=Entry(root,textvariable=dest,font=1,width=35)
    entr_dest.grid(row=4,column=1)
    dest.set(data)
def handler_english(e):
    src_data=var.get()
    res=t.translate(src_data,"en")
    data=res.text
    dest=StringVar()
    entr_dest=Entry(root,textvariable=dest,font=1,width=35)
    entr_dest.grid(row=4,column=1)
    dest.set(data)

def handler_punjabi(e):
    src_data=var.get()
    res=t.translate(src_data,"Pa")
    data=res.text
    dest=StringVar()
    entr_dest=Entry(root,textvariable=dest,font=1,width=35)
    entr_dest.grid(row=4,column=1)
    dest.set(data)

def handler_german(e):
    src_data=var.get()
    res=t.translate(src_data,"de")
    data=res.text
    dest=StringVar()
    entr_dest=Entry(root,textvariable=dest,font=1,width=35)
    entr_dest.grid(row=4,column=1)
    dest.set(data)

def handler_french(e):
    src_data=var.get()
    res=t.translate(src_data,"fr")
    data=res.text
    dest=StringVar()
    entr_dest=Entry(root,textvariable=dest,font=1,width=35)
    entr_dest.grid(row=4,column=1)
    dest.set(data)
def handler_russian(e):
    src_data=var.get()
    res=t.translate(src_data,"ru")
    data=res.text
    dest=StringVar()
    entr_dest=Entry(root,textvariable=dest,font=1,width=35)
    entr_dest.grid(row=4,column=1)
    dest.set(data)

root=Tk()
root.geometry("760x430")
root.config(bg="orange")
t=Translator()

lblsrc=Label(root,text="Enter your Text",font=1,bg="pink",width=20,height=3)
lblsrc.grid(row=0,column=1)
lblsrc.grid(pady=(40,20))

var=StringVar()
entr1=Entry(root,textvariable=var,font=1,width=35)
entr1.grid(row=1,column=1)

btnHi=Button(root,text="Covert in Hindi",font=1,bg="yellow",width=20,height=3)
btnHi.bind("<Button-1>",handler_hindi)
btnHi.grid(row=2,column=0)
btnHi.grid(pady=(40,20))
btnHi.grid(padx=(20,20))

btnEn=Button(root,text="Covert in English",font=1,bg="yellow",width=20,height=3)
btnEn.bind("<Button-1>",handler_english)
btnEn.grid(row=2,column=1)
btnEn.grid(pady=(40,20))

btnPn=Button(root,text="Covert in Punjabi",font=1,bg="yellow",width=20,height=3)
btnPn.bind("<Button-1>",handler_punjabi)
btnPn.grid(row=2,column=2)
btnPn.grid(pady=(40,20))

btnGe=Button(root,text="Covert in German",font=1,bg="yellow",width=20,height=3)
btnGe.bind("<Button-1>",handler_german)
btnGe.grid(row=3,column=0)
btnGe.grid(pady=(40,20))
btnGe.grid(padx=(20,20))

btnFr=Button(root,text="Covert in French",font=1,bg="yellow",width=20,height=3)
btnFr.bind("<Button-1>",handler_french)
btnFr.grid(row=3,column=1)
btnFr.grid(pady=(40,20))

btnRu=Button(root,text="Covert in Russian",font=1,bg="yellow",width=20,height=3)
btnRu.bind("<Button-1>",handler_russian)
btnRu.grid(row=3,column=2)
btnRu.grid(pady=(40,20))

root.mainloop()