import binascii
from tkinter import *
import hashlib
import binascii
from register import *
import os,index,datetime,sys

from pyparsing import Word
import tkinter
from turtle import pos
from PIL import Image, ImageTk
from tkinter import messagebox

from search import ser
def clse():
    sys.exit() 
    root.destroy()

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

# def make_pass(phone):
# 	return hashlib.sha256(str.encode(phone.get())).hexdigest()

# def check_pass(phone,hash):
# 	if make_pass(phone.get())==hash:
# 		return True

def pos():
    ret=verifier()
    if ret==0:
        h=open("admin.txt",'r')
        
        for line in h:
            temp = line.split('|')
            if temp[0]==name.get() and verify_password(temp[1],phone.get()):
                
                # make_pass(phone)   if we give hash password it works
                # check_pass(phone,hash)
                messagebox.showwarning("success","Authorization Success.")
                root.destroy()
                rec()
                os.system('python option.py')
                break
        else:
            messagebox.showwarning("Warning","Employee id or password is incorrect.")
    else:
        messagebox.showwarning("Warning","Type Employee id and password.")
def verifier():
    a=b=0
    if not name.get():
        a=1
    if not phone.get():
        b=1
    if a==1 or b==1 :
        return 1
    else:
        return 0 


# def login_check():
#     global id
#     id = eid.get()
#     password = psw.get()
#     pos = binary_search('admin.txt', eid)
#     if pos == -1:
#         tkinter.messagebox.showinfo("Login","Username is incorrect. Please re-enter")
#         return(root)
#     else:
#         f2 = open("admin.txt",'r')
#         f2.seek(int (pos))
#         l = f2.readline()
#         l = l.rstrip()
#         word = l.split('|')
#         if(check_password(word[1], password)):
#             tkinter.messagebox.showinfo("Login", "Login Successful")
#             root.destroy()
#         else:
#             tkinter.messagebox.showinfo("Login","Incorrect password")
#             return(root)
#         f2.c
            
        
def rec():
    o=datetime.datetime.now()
    k=o.strftime("%Y:%m:%d | %H:%M:%S")
    rc=name.get()+" | "+k
    g=open("record.txt",'a')
    g.write(rc)
    g.close()

        
if __name__=="__main__":
    
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("POLICE FIR RECORD")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\criminal\\criminal\\images\\jail.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='#812ca8')
    name=StringVar()
    phone=StringVar()
       
    label=Label(root,text="L O G I N",font="bold",fg="dark blue")
    label.place(x=450,y=100)
    label1=Label(root,text="Username :",bg='light blue')
    label1.place(x=360,y=150)

    label2=Label(root,text="Password :",bg='light blue')
    label2.place(x=360,y=180)


    e1=Entry(root,textvariable=name)
    e1.place(x=460,y=150)

    e2=Entry(root,show='*',textvariable=phone)
    e2.place(x=460,y=180)
        
    b4=Button(root,text="Submit",command=pos,activebackground="pink",bg="light blue",width=30)
    b4.place(x=363,y=300)
    b3=Button(root,text="Close",command=clse,bg="light blue",activebackground="red",width=30)
    b3.place(x=363,y=340)
    root.mainloop()

