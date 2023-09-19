from tkinter import *
from PIL import Image,ImageTk

class Staff:

    def __init__(self,centerFrame):
        self.center = centerFrame
        self.staffFrame = Frame(self.center, pady=5, padx=5)
        self.staffFrame.grid(row=0,column=2, sticky='senw')
        self.img3 = Image.open('C:\\Users\\pc\\Student système managment\\images\\staff.png')
        self.img3.thumbnail((180,180))
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgStaff = Label(self.staffFrame, image = self.new_img3, pady=5, padx=5)
        self.imgStaff.pack()
        self.buttonStaff = Button(self.staffFrame, text='Staff Managment', command=self.OpenWindowStaff, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonStaff.pack()   


        
    def OpenWindowStaff(self):
        self.master = Toplevel()
        self.master.title('Staff Managment System')