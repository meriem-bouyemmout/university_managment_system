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







class inter_admin :
    def __init__(self,mast):
        self.master = mast
        self.Frameleft = Frame(self.master, width=500, bg='#CAE1FF')
        self.Frameleft.pack(side=LEFT, fill=Y)
        #############################################################################################
        self.UserName = Label(self.Frameleft,text='UserName', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.UserName.place(x=10,y=20, width=100, height=40)
        self.Password = Label(self.Frameleft,text='Password', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Password.place(x=10,y=70, width=100, height=40)
        self.Name = Label(self.Frameleft,text='Name', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Name.place(x=10,y=120, width=100, height=40)
      
        self.username = StringVar()
        self.passwd = StringVar()
        self.name = StringVar()
        
##################################

    


    
########################################################
        self.UserName = Entry(self.Frameleft,text='FirstName', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.username)
        self.UserName.config(justify="center")
        self.UserName.place(x=120,y=20, width=200, height=40)
        self.Password = Entry(self.Frameleft,text='LastName', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.passwd)
        self.Password.config(justify="center")
        self.Password.place(x=120,y=70, width=200, height=40)
        self.Name = Entry(self.Frameleft,text='Matricule', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.name)
        self.Name.config(justify="center")
        self.Name.place(x=120,y=120, width=200, height=40)

###########################################################################
        
        def on_focus_in(event):
         event.widget.config(fg='black', bg="#B0E2FF")
        def on_focus_out(event):
         event.widget.config(fg='#4F4F4F', bg="white") 

        self.UserName.bind("<FocusIn>", on_focus_in)
        self.UserName.bind("<FocusOut>", on_focus_out)
        self.Password.bind("<FocusIn>", on_focus_in)
        self.Password.bind("<FocusOut>", on_focus_out)
        self.Name.bind("<FocusIn>", on_focus_in)
        self.Name.bind("<FocusOut>", on_focus_out)

###############################################################################           

        self.buttonAdd=Button(self.Frameleft,text='Add', command=self.add, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonAdd.place(x=20,y=200, width=60, height=60)
        self.buttonUp=Button(self.Frameleft,text='Update', command=self.update, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonUp.place(x=100,y=200, width=60, height=60)
        self.buttonDel=Button(self.Frameleft,text='Delete', command=self.delete, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonDel.place(x=180,y=200, width=60, height=60)
        self.buttonRead=Button(self.Frameleft,text='Show', command=self.read, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonRead.place(x=260,y=200, width=60, height=60)
        self.buttonReset=Button(self.Frameleft,text='Reset', command=self.reset, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonReset.place(x=340,y=200, width=60, height=60)
#######################################################################################################

        self.buttonApp = Button(self.Frameleft,text='Show the app', command=self.OpenWindowStudent, bg='#1b9ea4', fg='white', font=('tahoma',10,'bold'))
        self.buttonApp.place(x=20,y=450, width=100, height=50)    

        ####################################### RIGHT ####################################################
        self.Frameright = Frame(self.master, width=800, bg='#CAE1FF')
        self.Frameright.pack(side=LEFT, fill=BOTH)
        ##################################################################################################
        self.Framerighttop = Frame(self.Frameright, height=50, bg='#CAE1FF', pady=5, padx=5)
         
        self.studentsearch = Entry(self.Framerighttop, fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), width=130)
        self.studentsearch.grid(row = 0, column = 0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.Framerighttop, text='Search', command=self.search, fg='white', bg='#6E7B8B', font=('tahoma',12,'bold'), width=10)
        self.buttonsearch.grid(row = 0, column = 1, sticky='nsew', pady=10, padx=10)
           
        self.Framerighttop.grid_columnconfigure(0, weight=1)
        self.Framerighttop.grid_columnconfigure(0, weight=1)  

        self.Framerighttop.pack(fill=X)

        ##################################################################################################

        self.frameView = Frame(self.Frameright, bg = 'Blue')
        self.frameView.pack(fill=BOTH)

        self.scrollbar = Scrollbar(self.frameView, orient = VERTICAL)
        

        self.table = ttk.Treeview(self.frameView, column= ("ID","UserName","Password","Name"), show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview())       
        self.table.pack(fill=BOTH)
         


        self.table.heading("ID",text="ID")
        self.table.heading("UserName",text="UserName")
        self.table.heading("Password",text="Password")
        self.table.heading("Name",text="Name")
        

        self.table.column("ID", anchor=W, width=5)
        self.table.column("UserName", anchor=W, width=6)
        self.table.column("Password", anchor=W, width=6)
        self.table.column("Name", anchor=W, width=6)
       

        self.read()
        self.table.bind("<ButtonRelease>", self.show)
###################################################################################
       

      
      
    def add(self):
        try:
          mydb = mc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'university',
            charset= 'utf8mb4'
          )
        except:
            mb.showerror("Failed connection","please open your xampp server")  
        mycursor = mydb.cursor()
        req = " insert into loginadmin(Username, Password, Name) values (%s, %s, %s) "
        if (self.UserName.get() == '' or self.Password.get() == '' or self.Name.get() == '' ) :
          mb.showerror('Error','Complete all the blanks', parent=self.master)
                  
        else :  
          val = (self.UserName.get(), self.Password.get(), self.Name.get())          
          mycursor.execute(req, val)        
          mydb.commit()
          mydb.close() 
          mb.showinfo('Successfuly added','Data inserted Successfuly', parent=self.master)
          self.read()

          self.UserName.delete(0,'end')
          self.Password.delete(0,'end')
          self.Name.delete(0,'end') 


    def read(self):
        try:  
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
        req = " select * from loginadmin "
        mycursor.execute(req)
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())

        for i in result :
          self.table.insert('','end', iid=i[0], values=i)
          mydb.commit()
        mydb.close()  
               

    def show(self,ev): 
        self.data = self.table.focus()
        alldata = self.table.item(self.data)
        val = alldata['values']
        self.username.set(val[1])
        self.passwd.set(val[2])
        self.name.set(val[3])
        


    def reset(self):
        self.UserName.delete(0,'end')
        self.Password.delete(0,'end')
        self.Name.delete(0,'end')  
       
    def delete(self):
        try:
          mydb = mc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'university',
            charset= 'utf8mb4'
          )
        except:
            mb.showerror("Failed connection","please opeb your xampp server")  
        mycursor = mydb.cursor()
        req = ("delete from loginadmin where ID="+self.data)
        mycursor.execute(req)
        mydb.commit()
        mydb.close()
        mb.showinfo('Delete', 'The user was deleted', parent=self.master)
        self.read()
        self.reset()

    def update(self):
        try:
          mydb = mc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'university',
            charset= 'utf8mb4'
          )
        except:
            mb.showerror("Failed connection","please open your xampp server")  
        mycursor = mydb.cursor()

        if (self.username.get() == '' or self.passwd.get() == '' or self.name.get() == '' ) :
          mb.showerror('Error','Complete all the blanks', parent=self.master)
          
        
        else:

          req = ("update loginadmin set Username=%s, Password=%s, Name=%s where ID=%s ")
          val = (self.username.get(), self.passwd.get(), self.name.get(), self.data)
          mycursor.execute(req, val)
          mydb.commit()
          mydb.close()
          mb.showinfo('Update', 'The user was updated', parent=self.master)
          self.read()
          self.reset() 
           
    def search(self):
        try:           
          mydb = mc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'university',
            charset= 'utf8mb4'
          )
        except:
            mb.showerror("Failed connection","please open your xampp server")  
        mycursor = mydb.cursor()
        req = (" select * from loginadmin where ID="+self.studentsearch.get())
        mycursor.execute(req)
        result = mycursor.fetchone()
        if (result == None) :
           mb.showerror('Error','The user not exist', parent=self.master) 
           print(result)  
                
        else  :
          
          print(result)
          self.table.delete(*self.table.get_children()) 
          self.table.insert('','end', iid=result[0], values=result)
          mydb.commit()
          mydb.close()

    def OpenWindowStudent(self):
        
        win = Toplevel()
        win.iconbitmap('C:\\Users\\pc\\Student système managment\\images\\swim_ring_icon_183313.ico')
        uni = University(win)      
          