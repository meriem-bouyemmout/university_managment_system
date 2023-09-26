from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb

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
        stdw = StudentWindow()
        
class StudentWindow :
      def __init__(self):
        self.master = Toplevel()
        self.master.title('Student Managment System')
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        ################################# LEFT #######################################################
        self.Frameleft = Frame(self.master, width=500)
        self.Frameleft.pack(side=LEFT, fill=Y)
        #############################################################################################
        self.FirstName = Label(self.Frameleft,text='FirstName', fg='#4F4F4F', font=('tahoma',12,'bold'))
        self.FirstName.place(x=10,y=20, width=100, height=40)
        self.LastName = Label(self.Frameleft,text='LastName', fg='#4F4F4F', font=('tahoma',12,'bold'))
        self.LastName.place(x=10,y=70, width=100, height=40)
        self.Matricule = Label(self.Frameleft,text='Matricule', fg='#4F4F4F', font=('tahoma',12,'bold'))
        self.Matricule.place(x=10,y=120, width=100, height=40)
        self.Email = Label(self.Frameleft,text='Email', fg='#4F4F4F', font=('tahoma',12,'bold'))
        self.Email.place(x=10,y=170, width=100, height=40)
        self.Phone = Label(self.Frameleft,text='Phone', fg='#4F4F4F', font=('tahoma',12,'bold'))
        self.Phone.place(x=10,y=220, width=100, height=40)
        self.first = StringVar()
        self.last = StringVar()
        self.matr = StringVar()
        self.mail = StringVar()
        self.ph = StringVar()

        self.FirstName = Entry(self.Frameleft,text='FirstName', fg='#4F4F4F', font=('tahoma',12,'bold'), textvariable = self.first)
        self.FirstName.place(x=120,y=20, width=200, height=40)
        self.LastName = Entry(self.Frameleft,text='LastName', fg='#4F4F4F', font=('tahoma',12,'bold'), textvariable = self.last)
        self.LastName.place(x=120,y=70, width=200, height=40)
        self.Matricule = Entry(self.Frameleft,text='Matricule', fg='#4F4F4F', font=('tahoma',12,'bold'), textvariable = self.matr)
        self.Matricule.place(x=120,y=120, width=200, height=40)
        self.Email = Entry(self.Frameleft,text='Email', fg='#4F4F4F', font=('tahoma',12,'bold'), textvariable = self.mail)
        self.Email.place(x=120,y=170, width=200, height=40)
        self.Phone = Entry(self.Frameleft,text='Phone', fg='#4F4F4F', font=('tahoma',12,'bold'), textvariable = self.ph)
        self.Phone.place(x=120,y=220, width=200, height=40)


        self.add=Button(self.Frameleft,text='Add', command=self.add, fg='#4F4F4F', font=('tahoma',10,'bold'))
        self.add.place(x=40,y=300, width=60, height=60)
        self.add=Button(self.Frameleft,text='Update', fg='#4F4F4F', font=('tahoma',10,'bold'))
        self.add.place(x=170,y=300, width=60, height=60)
        self.add=Button(self.Frameleft,text='Delete', fg='#4F4F4F', font=('tahoma',10,'bold'))
        self.add.place(x=290,y=300, width=60, height=60)

        ####################################### RIGHT ####################################################
        self.Frameright = Frame(self.master, width=800)
        self.Frameright.pack(side=LEFT, fill=BOTH)
        ##################################################################################################
        self.Framerighttop = Frame(self.Frameright, height=50, pady=5, padx=5)
         
        self.studentsearch = Entry(self.Framerighttop, fg='#4F4F4F', font=('tahoma',12,'bold'), width=130)
        self.studentsearch.grid(row = 0, column = 0, sticky='nsew', pady=10, padx=10)
        self.buttonsearch = Button(self.Framerighttop, text='Search', fg='#4F4F4F', font=('tahoma',12,'bold'), width=10)
        self.buttonsearch.grid(row = 0, column = 1, sticky='nsew', pady=10, padx=10)
           
        self.Framerighttop.grid_columnconfigure(0, weight=1)
        self.Framerighttop.grid_columnconfigure(0, weight=1)  

        self.Framerighttop.pack(fill=X)

        ##################################################################################################

        self.frameView = Frame(self.Frameright, bg = 'Blue')
        self.frameView.pack(fill=BOTH)

        self.table = ttk.Treeview(self.frameView, column= ("ID","Firstname","Lastname","Matricule","Email","Phone"), show='headings')
        self.table.pack(fill=BOTH)

        self.table.heading("ID",text="ID")
        self.table.heading("Firstname",text="Firstname")
        self.table.heading("Lastname",text="Lastname")
        self.table.heading("Matricule",text="Matricule")
        self.table.heading("Email",text="Email")
        self.table.heading("Phone",text="Phone")

        self.table.column("ID", anchor=W, width=5)
        self.table.column("Firstname", anchor=W, width=6)
        self.table.column("Lastname", anchor=W, width=6)
        self.table.column("Matricule", anchor=W, width=6)
        self.table.column("Email", anchor=W, width=6)
        self.table.column("Phone", anchor=W, width=6)

        self.read()
        self.table.bind("<ButtonRelease>", self.show)
      
      
      def add(self):
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = " insert into student(Fistname, Lastname, Matricule, Email, Phone) values (%s, %s, %s, %s, %s) "
        if (self.FirstName.get() == '' or self.LastName.get() == '' or self.Matricule.get() == '' or self.Email.get() == '' or self.Phone.get() == '') :
          mb.showerror('Error','Complete all the blanks')
          
        else :
            if ( not self.FirstName.get().isalpha()  or not self.LastName.get().isalpha() or not self.Matricule.get().isdigit() or not self.Email.get().isalpha() or not self.Phone.get().isdigit() ) :
              mb.showerror('Error','Give us the true information') 

            else :  
              val = (self.FirstName.get(), self.LastName.get(), self.Matricule.get(), self.Email.get(), self.Phone.get())          
              mycursor.execute(req, val)        
              mydb.commit()
              mydb.close() 
              mb.showinfo('Successfuly added','Data inserted Successfuly')
              self.read()

              self.FirstName.delete(0,'end')
              self.LastName.delete(0,'end')
              self.Matricule.delete(0,'end')
              self.Email.delete(0,'end')
              self.Phone.delete(0,'end') 


      def read(self):  
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = " select * from student "
        mycursor.execute(req)
        result = mycursor.fetchall()
        self.table.delete(*self.table.get_children())

        for i in result :
          self.table.insert('','end',values=i)
          mydb.commit()
        mydb.close()  
               

      def show(self,ev): 
        data = self.table.focus()
        alldata = self.table.item(data)
        val = alldata['values']
        self.first.set(val[1])
        self.last.set(val[2])
        self.matr.set(val[3])
        self.mail.set(val[4])
        self.ph.set(val[5])