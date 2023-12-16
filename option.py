from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    root.destroy()
    os.system('python index.py')
def search():
    root.destroy()
    os.system('python search.py')
   
def add():
    root.destroy()
    os.system('python add.py')

def update():
    root.destroy()
    os.system('python update.py')

def delet():
    root.destroy()
    os.system('python delet.py')

def view():
    root.destroy()
    os.system('python view.py')
        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(435, 455)
    root.title("POLICE FIR RECORD")
    root.configure(bg='#00008B')
    root.configure(bg='#68BBE3')
    root = Canvas(root,width = 1980, height = 1080)
    root.pack()
    image = PhotoImage(file='C:\\criminal\\criminal\\images\\one.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='white')



   
    b1=Button(root,text="ADD INFO",command=add,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=100)
    b1=Button(root,text="UPDATE INFO",command=update,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=150)
    b1=Button(root,text="DELETE INFO",command=delet,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=200)
    b1=Button(root,text="VIEW ALL",command=view,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=250)
    b1=Button(root,text="SEARCH",command=search,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=300)
    b1=Button(root,text="LOGOUT",command=clse,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=350)
  
    
    root.mainloop()

