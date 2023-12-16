from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def delete_patient():
    if not cn.get():
        messagebox.showwarning("Warning","Fill the blank spaces.")
    else:
        dele.pos(cn.get())
        
        messagebox.showwarning("Succes","Deleted Successfully.")

        

                    





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("POLICE FIR RECORD")
    root.configure(bg='#68BBE3')

   
    label=Label(root,text="DELETE",font="bold",fg="Red")
    label.place(x=450,y=50)

    cn=StringVar()


    label2=Label(root,text="CONVICT NUMBER:")
    label2.place(x=300,y=170)





    e2=Entry(root,textvariable=cn,width=40)
    e2.place(x=420,y=170)

   
    b4=Button(root,text="Delete",command=delete_patient,activebackground="red",bg="#68BBE3",width=30)
    b4.place(x=363,y=240)
    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

