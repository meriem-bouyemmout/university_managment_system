from tkinter import *
from PIL import Image,ImageTk
import Student as st
import Staff as sf
import Library as lib
import Exam as ex



class University:
    def __init__(self,mast):
        self.master = mast
        self.master.title("University Systeme Managemment")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        #=========================university management system=======================================#
        self.frametop = Frame(self.master,bg='#1b9ea4',height=200)
        self.frametop.pack(fill=X)
        self.sms = Label(self.frametop,text="University Management Systeme",bg='#1b9ea4',fg='white',font=('tahoma',40),pady=45)
        self.sms.pack()
        #=======================center frame=========================================================#
        self.center = Frame(self.master)
        self.center.pack(fill=X)

        #=====================    info university   =========================================================#
               
        self.infoUniversity = Frame(self.center, pady=5,padx=5)
        self.infoUniversity.grid(row=0,column=0, sticky='senw')    
        self.img = Image.open('C:\\Users\\pc\\Student système managment\\images\\university.png')
        self.img.thumbnail((180,180))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.infoUniversity, image = self.new_img, pady=5, padx=5)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.infoUniversity, text='About University', bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonUniversity.pack()

        #=====================       student     =========================================================#

        self.studentFrame = Frame(self.center,padx=5,pady=5)
        self.studentFrame.grid(row=0,column=1, sticky='senw')
        self.img2 = Image.open('C:\\Users\\pc\\Student système managment\\images\\studenticon.png')
        self.img2.thumbnail((180,180))
        self.new_img2 = ImageTk.PhotoImage(self.img2)
        self.imgStudent = Label(self.studentFrame, image = self.new_img2, pady=5, padx=5)
        self.imgStudent.pack()
        self.buttonStudent = Button(self.studentFrame, text='Student Managment',command= self.OpenWindowStudent, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonStudent.pack()   

        #=====================      staff        =========================================================#

        self.staffFrame = Frame(self.center, pady=5, padx=5)
        self.staffFrame.grid(row=0,column=2, sticky='senw')
        self.img3 = Image.open('C:\\Users\\pc\\Student système managment\\images\\staff.png')
        self.img3.thumbnail((180,180))
        self.new_img3 = ImageTk.PhotoImage(self.img3)
        self.imgStaff = Label(self.staffFrame, image = self.new_img3, pady=5, padx=5)
        self.imgStaff.pack()
        self.buttonStaff = Button(self.staffFrame, text='Staff Managment', command=self.OpenWindowStaff, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonStaff.pack()   


        #=================================================================================================#
        self.center.grid_columnconfigure(0,weight=1)
        self.center.grid_columnconfigure(1,weight=1)
        self.center.grid_columnconfigure(2,weight=1) 
        #====================================Bottom frame===================================================#
        
        self.bottom = Frame(self.master)
        self.bottom.pack(fill=X)

        #==================================== Library fram ==================================================#

        self.libraryFrame = Frame(self.bottom, pady=5,padx=5)
        self.libraryFrame.grid(row=1,column=0, sticky='senw')    
        self.img4 = Image.open('C:\\Users\\pc\\Student système managment\\images\\open-book.png')
        self.img4.thumbnail((180,180))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.libraryFrame, image = self.new_img4, pady=5, padx=5)
        self.imgLibrary.pack()
        self.buttonLibrary = Button(self.libraryFrame, text='About Library',command=self.OpenWindowLibrary, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonLibrary.pack()

        #===================================== Examen =======================================================#

        self.examenFrame = Frame(self.bottom, pady=5,padx=5)
        self.examenFrame.grid(row=1,column=1, sticky='senw')    
        self.img5 = Image.open('C:\\Users\\pc\\Student système managment\\images\\exam.png')
        self.img5.thumbnail((180,180))
        self.new_img5 = ImageTk.PhotoImage(self.img5)
        self.imgExamen = Label(self.examenFrame, image = self.new_img5, pady=5, padx=5)
        self.imgExamen.pack()
        self.buttonExamen = Button(self.examenFrame, text='Exam', command=self.OpenWindowExam, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonExamen.pack() 

        
        self.bottom.grid_columnconfigure(0,weight=1)
        self.bottom.grid_columnconfigure(1,weight=1)


    def OpenWindowStudent(self):
        std = st.Student()
    def OpenWindowStaff(self):
        std = sf.Staff() 
    def OpenWindowLibrary(self):
        std = lib.Library()
    def OpenWindowExam(self):
        std = ex.Exam()    





if (__name__ == '__main__'):
    window = Tk()
    std = University(window)
    mainloop()