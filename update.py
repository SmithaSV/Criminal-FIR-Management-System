from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
import dele
def clse():
    root.destroy()
    os.system('python option.py')



def verifier():
    a=b=c=d=e=f=0
    if not name.get():
        #t1.insert(END,"<>Name is required<>\n")
        a=1
    if not cn.get():
        #t1.insert(END,"<>Adhar no is required<>\n")
        b=1
    if not age.get():
        #t1.insert(END,"<>Age is required<>\n")
        c=1
    if not phone.get():
        #t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not crime.get():
       #t1.insert(END,"<>Covid test result name is required<>\n")
        e=1
    if not address.get():
        #t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        messagebox.showwarning("Warning","Fill the blank spaces.")
        return 1
    else:
        return 0


        

def ad():
    t1=datetime.datetime.now()
    m1=t1.strftime("%Y:%m:%d - %H:%M:%S")
    ls=name.get()+'|'+cn.get()+'|'+age.get()+'|'+phone.get()+'|'+crime.get()+'|'+address.get()+'|'+m1+"\n"
    
    p=open('criminal.txt','a')
    p.write(ls)
    p.close()
                    


def add_patient():
            ret=verifier()
            if ret==0:
                ad()
                messagebox.showwarning("Succes","Added Successfully.")
                                 

def update_patient():
    ret=verifier()
    if ret==0:
        dele.pos(cn.get())
        
        ad()
        messagebox.showwarning("Succes","Updated successfully")


        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("POLICE FIR RECORD")
    root.configure(bg='#68BBE3')

   
    label=Label(root,text="UPDATE DETAILS",font="bold",fg="Red")
    label.place(x=450,y=50)
    name=StringVar()
    cn=StringVar()
    age=StringVar()
    phone=StringVar()
    crime=StringVar()
    address=StringVar()
    
    label1=Label(root,text="CONVICT NAME:")
    label1.place(x=300,y=120)

    label2=Label(root,text="CONVICT NUMBER:")
    label2.place(x=300,y=170)

    label3=Label(root,text="AGE:")
    label3.place(x=300,y=220)

    label4=Label(root,text="PHONE NUMBER:")
    label4.place(x=300,y=270)

    label5=Label(root,text="CRIME:")
    label5.place(x=300,y=320)

    label6=Label(root,text="ADDRESS:")
    label6.place(x=300,y=370)

    e1=Entry(root,textvariable=name,width=40)
    e1.place(x=420,y=120)

    e2=Entry(root,textvariable=cn,width=40)
    e2.place(x=420,y=170)

    e3=Entry(root,textvariable=age,width=40)
    e3.place(x=420,y=220)

    e4=Entry(root,textvariable=phone,width=40)
    e4.place(x=420,y=270)
    
    e5=Entry(root,textvariable=crime,width=40)
    e5.place(x=420,y=320)

    e6=Entry(root,textvariable=address,width=40)
    e6.place(x=420,y=370)
   
    b4=Button(root,text="Submit",command=update_patient,activebackground="pink",bg="#68BBE3",width=30)
    b4.place(x=363,y=420)
    b3=Button(root,text="Back",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=700,y=420)
    root.mainloop()

