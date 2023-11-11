from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
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
        self.buttonLogout = Button(self.frametop, text='Logout', command=self.Logout)
        self.buttonLogout.pack()
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
        self.bottom.grid_columnconfigure(0,weight=1)
        self.bottom.grid_columnconfigure(1,weight=1)

    def Logout(self):
        self.master.destroy()


class Login :
    def __init__(self,mast):
        self.master = mast
        self.master.title("Login Page")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")

        self.img = Image.open('C:\\Users\\pc\\Student système managment\\images\\loginImage.png')
        self.img.thumbnail((200,200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgLogin = Label(self.master, image=self.new_img)
        self.imgLogin.pack(pady = 50)

        self.frameLogin = Frame(self.master)
        self.frameLogin.pack()
        self.usernameLabel = Label(self.frameLogin, text = 'Username', pady=10, padx=10, font=('tahoma',12,'bold'))
        self.usernameLabel.grid(row=0, column=0)
        self.passwordLabel = Label(self.frameLogin, text = 'Password', pady=10, padx=10, font=('tahoma',12,'bold'))
        self.passwordLabel.grid(row=1, column=0)
        self.username = Entry(self.frameLogin, fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'))
        self.username.config(justify="center")
        self.username.grid(row=0, column=1, pady=10, padx=10)
        self.password = Entry(self.frameLogin, fg='#4F4F4F', bg='white', show='*', font=('tahoma',12,'bold'))
        self.password.config(justify="center")
        self.password.grid(row=1, column=1, pady=10, padx=10)
        self.buttonLogin=Button(self.frameLogin, text='Login', command=self.Login, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'), cursor='cross')
        self.buttonLogin.grid(row=2, column=0, columnspan=2, sticky='snew', padx=10, pady=10)


    def Login(self):
        try :
            mydb = mc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'university',
            charset= 'utf8mb4'
            )
        except:
            mb.showerror("Failed connection","please opner your xampp server")    
        mycursor = mydb.cursor()
        req = " select * from LoginAdmin where username = '"+self.username.get()+"' and password = '"+self.password.get()+"' "
        mycursor.execute(req)
        result = mycursor.fetchone()
        if (result == None) :
            mb.showerror('Erreur','Invalaid username and password')  
            self.username.delete(0,'end')
            self.password.delete(0,'end')
        else :         
            win = Toplevel()
            win.iconbitmap('C:\\Users\\pc\\Student système managment\\images\\swim_ring_icon_183313.ico')
            uni = University(win)
            self.username.delete(0,'end')
            self.password.delete(0,'end')   
        
        mydb.commit()



        


             




if (__name__ == '__main__'):
    window = Tk()
    window.iconbitmap('C:\\Users\\pc\\Student système managment\\images\\swim_ring_icon_183313.ico')
    std = Login(window)
    mainloop()