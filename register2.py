import hashlib
from tkinter import *
import tkinter.font
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    root.destroy()
    os.system('python index.py')
def log():
	root.destroy()
	os.system('python login.py')


def verifier():
    a=b=c=d=0
    if not name.get():
        #t1.insert(END,"<>Name is required<>\n")
        a=1
    if not cn.get():
        #t1.insert(END,"<>Customer ID is required<>\n")
        b=1
    if not age.get():
        #t1.insert(END,"<>Address is required<>\n")
        c=1
    if not phone.get():
        #t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    # if not product_name.get():
    #    #t1.insert(END,"<>Product name is required<>\n")
    #     e=1
    # if not units.get():
    #     #t1.insert(END,"<>Units is Required<>\n")
    #     f=1
    if a==1 or b==1 or c==1 or d==1: #or e==1 or f==1:
        messagebox.showwarning("Warning","Fill the blank spaces.")
        return 1
    else:
        return 0

# def ad():
# 	f = open('admin.txt', 'a')
# 	pos = f.tell()
# 	buf = customer_name.get() + '|' + hashlib.sha256(str.encode(phone.get())).hexdigest() + '|' + '#' 
# 	f.write(buf)
# 	f.write('\n')
# 	f.close()
# 	tkinter.messagebox.showinfo("Register", "Registration successful!")
def ad():
	f = open('admin.txt', 'a')
	pos = f.tell()
	buf = name.get() + '|' + hashlib.sha256(str.encode(cn.get())).hexdigest() + '|' + '#' 
	f.write(buf)
	f.write('\n')
	f.close()
	tkinter.messagebox.showinfo("Register", "Registration successful!")
        
        



# def fakead():
#     fakels=customer_name.get()+'|'+customer_id.get()+'|'+address.get()+'|'+phone.get()+'|'+product_name.get()+'|'+units.get()+"#\n"
    
#     p=open('products2.txt','a')
#     p.write(fakels)
#     p.close()
                        


def add_products():
            ret=verifier()
            if ret==0:
                ad()
                # fakead()
                messagebox.showwarning("Success","Added Successfully.")
                                 
# def sorting(filename):
#     infile = open('products2.txt', 'r')
#     words = []
#     for line in infile:
#         temp = line.split()
#         for i in temp:
#             words.append(i)
#         #words.append('\n')    
#     infile.close()
#     words.sort()
#     outfile = open("result.txt", "w")
#     for i in words:
#         outfile.writelines(i)
#         outfile.writelines('\n')
#     outfile.close()

def binary_search(fname, search_key):
	t = []
	fin = open(fname,'r')
	for lx in fin:
		lx = lx.rstrip()
		wx = lx.split('|')
		t.append((wx[0], wx[1]))
	fin.close()
	l = 0
	r = len(t) - 1
	while l <= r:
		mid = (l + r)//2
		if t[mid][0] == search_key:
			return int(t[mid][1])
		elif t[mid][0] <= search_key:
			l = mid + 1
		else:
			r = mid - 1
	return -1





        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("")
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='#812ca8')

   
    label=Label(root,text="Enter your details",font="bold",fg="Blue")
    label.place(x=420,y=90)
    name=StringVar()
    cn=StringVar()
    age=StringVar()
    phone=StringVar()
    
    
    label1=Label(root,text="Username:",bg='light blue')
    label1.place(x=250,y=120)

    label2=Label(root,text="Phone number:",bg='light blue')
    label2.place(x=250,y=170)

    label3=Label(root,text="Email:",bg='light blue')
    label3.place(x=250,y=220)

    label4=Label(root,text="Password:",bg='light blue')
    label4.place(x=250,y=270)

    # label5=Label(root,text="Email:",bg='light blue')
    # label5.place(x=250,y=320)

    # label6=Label(root,text="Password:",bg='light blue')
    # label6.place(x=250,y=370)

    e1=Entry(root,textvariable=customer_name,width=40)
    e1.place(x=420,y=120)

    e2=Entry(root,textvariable=customer_id,width=40)
    e2.place(x=420,y=170)

    e3=Entry(root,textvariable=address,width=40)
    e3.place(x=420,y=220)

    e4=Entry(root,textvariable=phone,width=40)
    e4.place(x=420,y=270)
    
    # e5=Entry(root,textvariable=product_name,width=40)
    # e5.place(x=420,y=320)

    # e6=Entry(root,textvariable=units,width=40)
    # e6.place(x=420,y=370)
   
    b4=Button(root,text="Submit",command=add_products,activebackground="blue",bg="#6292c4",width=30)
    b4.place(x=363,y=420)

    # sorting('products.txt')

    b3=Button(root,text="Back",command=clse,bg="#6292c4",activebackground="red",width=30)
    b3.place(x=650,y=420)
    root.mainloop()

