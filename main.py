from tkinter import *
import infoUniversity as infuniv
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
        infunivv = infuniv.infoUniversity(self.center)       
        #=====================       student     =========================================================#
        std = st.Student(self.center)     
        #=====================      staff        =========================================================#
        stf = sf.Staff(self.center)
        #====================================Bottom frame===================================================#
        
        self.bottom = Frame(self.master)
        self.bottom.pack(fill=X)

        #==================================== Library fram ==================================================#
        libb = lib.Library(self.bottom)
        #===================================== Examen =======================================================#
        exx = ex.Exam(self.bottom)
        #====================================================================================================#

        self.center.grid_columnconfigure(0,weight=1)
        self.center.grid_columnconfigure(1,weight=1)
        self.center.grid_columnconfigure(2,weight=1)
        self.center.grid_columnconfigure(0,weight=1)
        self.center.grid_columnconfigure(1,weight=1)
         
         

             




if (__name__ == '__main__'):
    window = Tk()
    std = University(window)
    mainloop()