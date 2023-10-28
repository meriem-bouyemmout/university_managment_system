from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb


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
        stdw = StaffWindow()

class StaffWindow :
    def __init__(self):
        self.master = Toplevel()
        self.master.title('Staff Management System')
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        ################################# LEFT #######################################################
        self.Frameleft = Frame(self.master, width=500, bg='#CAE1FF')
        self.Frameleft.pack(side=LEFT, fill=Y)
        #############################################################################################
        self.FirstName = Label(self.Frameleft,text='FirstName', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.FirstName.place(x=10,y=20, width=100, height=40)
        self.LastName = Label(self.Frameleft,text='LastName', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.LastName.place(x=10,y=70, width=100, height=40)
        self.Matricule = Label(self.Frameleft,text='Matricule', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Matricule.place(x=10,y=120, width=100, height=40)
        self.job = Label(self.Frameleft,text='job', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.job.place(x=10,y=170, width=100, height=40)
        self.Email = Label(self.Frameleft,text='Email', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Email.place(x=10,y=220, width=100, height=40)
        self.Phone = Label(self.Frameleft,text='Phone', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Phone.place(x=10,y=270, width=100, height=40)
        
        self.first = StringVar()
        self.last = StringVar()
        self.matr = StringVar()
        self.jb = StringVar()
        self.mail = StringVar()
        self.ph = StringVar()

######################################################################################
        def set_combobox_fg(combobox, color):
         # Créez un style personnalisé pour le Combobox
         style = ttk.Style()
         style.configure('Custom.TCombobox', foreground=color)

        # Appliquez le style personnalisé au Combobox
         combobox['style'] = 'Custom.TCombobox'

#########################################################################################
        self.FirstName = Entry(self.Frameleft,text='FirstName', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.first)
        self.FirstName.config(justify="center")
        self.FirstName.place(x=120,y=20, width=200, height=40)
        self.LastName = Entry(self.Frameleft,text='LastName', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.last)
        self.LastName.config(justify="center")
        self.LastName.place(x=120,y=70, width=200, height=40)
        self.Matricule = Entry(self.Frameleft,text='Matricule', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.matr)
        self.Matricule.config(justify="center")
        self.Matricule.place(x=120,y=120, width=200, height=40)     
        self.job = ttk.Combobox(self.Frameleft,text='job', values=["","Chef departemment", "Chef de service", "Secrétère", "Ingénieur", "Technicien", "Prof", "Agent", "Employé"], state = 'readonly', font=('tahoma',12,'bold'), textvariable = self.jb)
        self.job.config(justify="center")
        set_combobox_fg(self.job, "#4F4F4F")
        self.job.place(x=120,y=170, width=200, height=40)
        self.Email = Entry(self.Frameleft,text='Email', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.mail)
        self.Email.config(justify="center")
        self.Email.place(x=120,y=220, width=200, height=40)
        self.Phone = Entry(self.Frameleft,text='Phone', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.ph)
        self.Phone.config(justify="center")
        self.Phone.place(x=120,y=270, width=200, height=40)

        

        def on_focus_in(event):
         event.widget.config(fg='black', bg="#B0E2FF")
        def on_focus_out(event):
         event.widget.config(fg='#4F4F4F', bg="white") 

        self.FirstName.bind("<FocusIn>", on_focus_in)
        self.FirstName.bind("<FocusOut>", on_focus_out)
        self.LastName.bind("<FocusIn>", on_focus_in)
        self.LastName.bind("<FocusOut>", on_focus_out)
        self.Matricule.bind("<FocusIn>", on_focus_in)
        self.Matricule.bind("<FocusOut>", on_focus_out)
       
        self.Email.bind("<FocusIn>", on_focus_in)
        self.Email.bind("<FocusOut>", on_focus_out)
        self.Phone.bind("<FocusIn>", on_focus_in)
        self.Phone.bind("<FocusOut>", on_focus_out)

###############################################################################         


        self.buttonAdd=Button(self.Frameleft,text='Add', command=self.add, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonAdd.place(x=20,y=350, width=60, height=60)
        self.buttonUp=Button(self.Frameleft,text='Update', command=self.update, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonUp.place(x=100,y=350, width=60, height=60)
        self.buttonDel=Button(self.Frameleft,text='Delete', command=self.delete, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonDel.place(x=180,y=350, width=60, height=60)
        self.buttonRead=Button(self.Frameleft,text='Show', command=self.read, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonRead.place(x=260,y=350, width=60, height=60)
        self.buttonReset=Button(self.Frameleft,text='Reset', command=self.reset, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonReset.place(x=340,y=350, width=60, height=60)
    

        ####################################### RIGHT ####################################################
        self.Frameright = Frame(self.master, width=800, bg='#CAE1FF')
        self.Frameright.pack(side=LEFT, fill=BOTH)
        ##################################################################################################
        self.Framerighttop = Frame(self.Frameright, bg='#CAE1FF', height=50, pady=5, padx=5)
         
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
        

        self.table = ttk.Treeview(self.frameView, column= ("ID","Firstname","Lastname","Matricule","Job","Email","Phone"), show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview())       
        self.table.pack(fill=BOTH)
         


        self.table.heading("ID",text="ID")
        self.table.heading("Firstname",text="Firstname")
        self.table.heading("Lastname",text="Lastname")
        self.table.heading("Matricule",text="Matricule")
        self.table.heading("Job",text="Job")
        self.table.heading("Email",text="Email")
        self.table.heading("Phone",text="Phone")

        self.table.column("ID", anchor=W, width=3)
        self.table.column("Firstname", anchor=W, width=6)
        self.table.column("Lastname", anchor=W, width=6)
        self.table.column("Matricule", anchor=W, width=6)
        self.table.column("Job", anchor=W, width=6)
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
        req = " insert into staff(Fistname, Lastname, Matricule, Job, Email, Phone) values (%s, %s, %s, %s, %s, %s) "
        if (self.FirstName.get() == '' or self.LastName.get() == '' or self.Matricule.get() == '' or self.job.get() == '' or self.Email.get() == '' or self.Phone.get() == '') :
          mb.showerror('Error','Complete all the blanks', parent=self.master)
          
        else :
            if ( not self.FirstName.get().isalpha()  or not self.LastName.get().isalpha() or not self.Matricule.get().isdigit() or not self.Email.get().isalpha() or not self.Phone.get().isdigit() ) :
              mb.showerror('Error','Give us the true information', parent=self.master) 

            else :  
              val = (self.FirstName.get(), self.LastName.get(), self.Matricule.get(), self.job.get(), self.Email.get(), self.Phone.get())          
              mycursor.execute(req, val)        
              mydb.commit()
              mydb.close() 
              mb.showinfo('Successfuly added','Data inserted Successfuly', parent=self.master)
              self.read()
              self.reset()


    def read(self):  
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = " select * from staff "
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
        self.first.set(val[1])
        self.last.set(val[2])
        self.matr.set(val[3])
        self.jb.set(val[4])
        self.mail.set(val[5])
        self.ph.set(val[6])


    def reset(self):
        self.FirstName.delete(0,'end')
        self.LastName.delete(0,'end')
        self.Matricule.delete(0,'end')
        self.job.current(0)
        self.Email.delete(0,'end')
        self.Phone.delete(0,'end')   
       
    def delete(self):
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = ("delete from staff where ID="+self.data)
        mycursor.execute(req)
        mydb.commit()
        mydb.close()
        mb.showinfo('Delete', 'The employé was deleted', parent=self.master)
        self.read()
        self.reset()

    def update(self):
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()

        if (self.first.get() == '' or self.last.get() == '' or self.matr.get() == '' or self.job.get() == '' or self.mail.get() == '' or self.ph.get() == '') :
          mb.showerror('Error','Complete all the blanks', parent=self.master)
          
        else :
            if ( not self.first.get().isalpha()  or not self.last.get().isalpha() or not self.matr.get().isdigit() or not self.mail.get().isalpha() or not self.ph.get().isdigit() ) :
              mb.showerror('Error','Give us the true information', parent=self.master)         
         
            else:

              req = ("update staff set Fistname=%s, Lastname=%s, Matricule=%s, Job=%s, Email=%s, Phone=%s where ID=%s ")
              val = (self.first.get(), self.last.get(), self.matr.get(), self.jb.get(), self.mail.get(), self.ph.get(), self.data)
              mycursor.execute(req, val)
              mydb.commit()
              mydb.close()
              mb.showinfo('Update', 'The employé was updated', parent=self.master)
              self.read()
              self.reset() 
           
    def search(self):
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = (" select * from staff where ID="+self.studentsearch.get())
        mycursor.execute(req)
        result = mycursor.fetchone()


        if (result == None) :
           mb.showerror('Error','The employe not exist', parent=self.master) 
           print(result)  
                
        else  :
          
          print(result)
          self.table.delete(*self.table.get_children()) 
          self.table.insert('','end', iid=result[0], values=result)
          mydb.commit()
          mydb.close()  
                  