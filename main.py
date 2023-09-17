from tkinter import *
from PIL import Image,ImageTk

class Student:
    def __init__(self,mast):
        self.master = mast
        self.master.title("Student Systeme Managemment")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        #=========================university management system=======================================#
        self.frametop = Frame(self.master,bg='#1b9ea4',height=200)
        self.frametop.pack(fill=X)
        self.sms = Label(self.frametop,text="University Management Systeme",bg='#1b9ea4',fg='white',font=('tahoma',50),pady=80)
        self.sms.pack()
        #=======================center frame=========================================================#
        self.center = Frame(self.master,height=200)
        self.center.pack(fill=X)

        #=====================    info university   =========================================================#
               
        self.infoUniversity = Frame(self.center, pady=50,padx=50)
        self.infoUniversity.grid(row=0,column=0)    
        self.img = Image.open('C:\\Users\\pc\\Student système managment\\images\\university.png')
        self.img.thumbnail((200,200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.infoUniversity, image = self.new_img)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.infoUniversity, text='About University', bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonUniversity.pack()

        #=====================       student     =========================================================#

        self.studentFrame = Frame(self.center,padx=50,pady=50)
        self.studentFrame.grid(row=0,column=1)
        self.img2 = Image.open('C:\\Users\\pc\\Student système managment\\images\\studenticon.png')
        self.img2.thumbnail((200,200))
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgStudent = Label(self.studentFrame, image = self.new_img2)
        self.imgStudent.pack()
        self.buttonStudent = Button(self.studentFrame, text='Student Managment', bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonStudent.pack()   

        #=====================      staff        =========================================================#

        self.staffFrame = Frame(self.center, pady=50, padx=50)
        self.staffFrame.grid(row=0,column=2)
        self.img3 = Image.open('C:\\Users\\pc\\Student système managment\\images\\staff.png')
        self.img3.thumbnail((200,200))
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgStaff = Label(self.staffFrame, image = self.new_img3)
        self.imgStaff.pack()
        self.buttonStaff = Button(self.staffFrame, text='Staff Managment', bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonStaff.pack()   


        #=================================================================================================#
        self.center.grid_columnconfigure(0,weight=1)
        self.center.grid_columnconfigure(1,weight=1)
        self.center.grid_columnconfigure(2,weight=1) 




if (__name__ == '__main__'):
    window = Tk()
    std = Student(window)
    mainloop()