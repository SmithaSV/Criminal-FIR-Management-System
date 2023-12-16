from tkinter import *
import os,index,datetime,sys
from PIL import Image, ImageTk
from tkinter import messagebox
def clse():
    sys.exit() 
def pos():
    root.destroy()
    os.system('python login.py')
def ros():
    root.destroy()
    os.system('python register.py')    
    




        
if __name__=="__main__":
    root=Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("POLICE FIR RECORD")
    root.configure(bg='#D4AC0D')
    root = Canvas(root,width = 935, height = 455)
    root.pack()
    image = PhotoImage(file='C:\\criminal\\criminal\\images\\one.png')
    root.create_image(0,0,anchor = NW, image = image)
    root.configure(bg='white')



   
    b1=Button(root,text="LOGIN HERE",command=pos,activebackground="pink",bg="#68BBE3",width=30)
    b1.place(x=363,y=200)
    b2=Button(root,text="REGISTER HERE",command=ros,activebackground="pink",bg="#68BBE3",width=30)
    b2.place(x=363,y=160)
    
    root.mainloop()


