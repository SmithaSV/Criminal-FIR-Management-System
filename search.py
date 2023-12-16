from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')

def ver():
    a=0
    if not name.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
        a=1
    return a


# def delete_patient():
#     if not op.get():
#         messagebox.showwarning("Warning","Fill the blank spaces.")
#     else:
#         dele.pos(op.get())
        
#         messagebox.showwarning("Succes","Deleted Successfully.")

def ser():
    t=ver()
    if (t==0):
        f=open("criminal.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(name.get())!=-1:
                t1.insert(END,"\n"+i+"\n")      

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("POLICE FIR RECORD")
    root.configure(bg='#68BBE3')

   
    label=Label(root,text="SEARCH",font="bold",fg="Red")
    label.place(x=450,y=50)

    name=StringVar()


    label2=Label(root,text="Name:")
    label2.place(x=300,y=170)





    e2=Entry(root,textvariable=name,width=40)
    e2.place(x=420,y=170)

   
    b4=Button(root,text="Search",command=ser,activebackground="red",bg="#68BBE3",width=30)
    b4.place(x=363,y=240)
    t1=Text(root,width=80,height=10)
    t1.place(x=10,y=280)
    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

