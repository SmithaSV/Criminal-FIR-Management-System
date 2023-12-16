from calendar import c
from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox

def pos():
    root.destroy()
    os.system('python login.py')
    
def clse():
    root.destroy()
    os.system('python option.py')



        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("POLICE FIR RECORD")
    root.configure(bg='#68BBE3')
    label=Label(root,text="CRIMINAL RECORD",font="bold",fg="Red")
    label.place(x=363,y=50)
    Name=[]
    cn=[]
    Age=[]
    crime=[]
    Address=[]
    ph=[]
    Date=[]
    norecord = 0
    f1 = open('criminal2.txt', 'r')
    for line in f1:
        norecord += 1
        line = line.rstrip('\n')
        word = line.split('|')
        Name.append(word[0])
        cn.append(word[1])
        Age.append(word[2])
        ph.append(word[3])
        crime.append(word[4])
        Address.append(word[5])
        # Date.append(word[6])
    f1.close()
    borrow_list=Listbox(root,height=50,width=20)
    borrow_list1=Listbox(root,height=50,width=10)
    borrow_list2=Listbox(root,height=50,width=10)
    borrow_list3=Listbox(root,height=50,width=20)
    borrow_list4=Listbox(root,height=50,width=20)
    borrow_list5=Listbox(root,height=50,width=40)
    borrow_list6=Listbox(root,height=50,width=40)
    for num in range(0,norecord):
        borrow_list.insert(0,Name[num])
        borrow_list1.insert(0,cn[num])
        borrow_list2.insert(0,Age[num])
        borrow_list3.insert(0,ph[num])
        borrow_list4.insert(0,crime[num])
        borrow_list5.insert(0,Address[num])
        # borrow_list6.insert(0,Date[num])
    borrow_list.configure(background="light grey")
    borrow_list1.configure(background="pink")
    borrow_list2.configure(background="pink")
    borrow_list3.configure(background="light grey")
    borrow_list4.configure(background="pink")
    borrow_list5.configure(background="light grey")
    # borrow_list6.configure(background="pink")

    borrow_label=Label(root,text="CONVICT NAME")
    borrow_label2=Label(root,text="CONVICT NUMBER")
    borrow_label3=Label(root,text="AGE")
    borrow_label4=Label(root,text="PHONE")
    borrow_label5=Label(root,text="CRIME")
    borrow_label6=Label(root,text="ADDRESS")
    # borrow_label7=Label(root,text="DATE")
	
    borrow_label.grid(row=3,column=0)
    borrow_label2.grid(row=3,column=1)
    borrow_label3.grid(row=3,column=4)
    borrow_label4.grid(row=3,column=7)
    borrow_label5.grid(row=3,column=8)
    borrow_label6.grid(row=3,column=10)
    # borrow_label7.grid(row=3,column=12)

    borrow_list.grid(row=4,column=0)
    borrow_list1.grid(row=4,column=1)
    borrow_list2.grid(row=4,column=4)
    borrow_list3.grid(row=4,column=7)
    borrow_list4.grid(row=4,column=8)
    borrow_list5.grid(row=4,column=10)
    borrow_list6.grid(row=4,column=12)

    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

