import binascii
import hashlib
from msilib.schema import File
from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox



def clse():
    sys.exit() 

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password    
def pos():
    ret=verifier()
    if ret==0:
        h=open("admin.txt", 'r')
        # lines = h.readlines()
        for line in h:
            temp = line.split('|')
            if temp[0]==name.get() and verify_password(temp[1],cn.get()):
             h.close()
        for i in h:
            if i.find(name.get())!=-1 and i.find(cn.get())!=-1:
                messagebox.showwarning("success","Authorization Success.")
                root.destroy()
                rec()
                
                os.system('python option.py')
                break
        else:
            messagebox.showwarning("Warning","Embloyee id or password is incorrect.")
    else:
        messagebox.showwarning("Warning","Type Embloyee id and password.")
def verifier():
    a=b=0
    if not name.get():
        a=1
    if not cn.get():
        b=1
    if a==1 or b==1 :
        return 1
    else:
        return 0  
        
def rec():
    o=datetime.datetime.now()
    k=o.strftime("%Y:%m:%d | %H:%M:%S")
    rc=cn.get()+" | "+k
    g=open("record.txt",'a')
    g.write(rc)
    g.close()

                  




        
if __name__=="__main__":
    root=Tk()
    root.minsize(930, 440)
    root.maxsize(1540, 770)
    root.title("POLICE FIR RECORD")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\criminal\\images\\logo.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='white')

    name=StringVar()
    cn=StringVar()
    label=Label(root,text="LOGIN",font="bold",fg="blue")
    
    label.place(x=450,y=50)
    label1=Label(root,text="Police id :")
    label1.place(x=360,y=120)

    label2=Label(root,text="Password      :")
    label2.place(x=360,y=150)


    e1=Entry(root,textvariable=name)
    e1.place(x=460,y=120)

    e2=Entry(root,show='*',textvariable=cn)
    e2.place(x=460,y=150)
   
    b4=Button(root,text="Submit",command=pos,activebackground="pink",bg="#ADD8E6",width=40)
    b4.place(x=363,y=200)
    b3=Button(root,text="Close",command=clse,bg="#68BBE3",activebackground="red",width=30)
    b3.place(x=600,y=380)
   
    root.mainloop()


