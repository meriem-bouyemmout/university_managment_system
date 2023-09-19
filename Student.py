from tkinter import *
from PIL import Image,ImageTk

class Student:
     def __init__(self,centerFrame):
        self.center = centerFrame
        self.studentFrame = Frame(self.center,padx=5,pady=5)
        self.studentFrame.grid(row=0,column=1, sticky='senw')
        self.img2 = Image.open('C:\\Users\\pc\\Student système managment\\images\\studenticon.png')
        self.img2.thumbnail((180,180))
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgStudent = Label(self.studentFrame, image = self.new_img2, pady=5, padx=5)
        self.imgStudent.pack()
        self.buttonStudent = Button(self.studentFrame, text='Student Managment',command= self.OpenWindowStudent, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonStudent.pack() 

     def OpenWindowStudent(self):
        self.master = Toplevel()
        self.master.title('Student Managment System')
        self.master.geometry('800x600+150+150')
           
