from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import mysql.connector as mc
import tkinter.messagebox as mb

class Exam:
    def __init__(self,bottomFrame):
        self.bottom = bottomFrame
        self.examenFrame = Frame(self.bottom, pady=5,padx=5)
        self.examenFrame.grid(row=1,column=1, sticky='senw')    
        self.img5 = Image.open('C:\\Users\\pc\\Student système managment\\images\\exam.png')
        self.img5.thumbnail((180,180))
        self.new_img5 = ImageTk.PhotoImage(self.img5)
        self.imgExamen = Label(self.examenFrame, image = self.new_img5, pady=5, padx=5)
        self.imgExamen.pack()
        self.buttonExamen = Button(self.examenFrame, text='Exam', command=self.OpenWindowExam, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonExamen.pack()


    def OpenWindowExam(self):
        stdw = ExamWindow()


class ExamWindow :

    def __init__(self):
        self.master = Toplevel()
        self.master.title('Student Management System')
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        ############################## backgound#########################################
       

        ################################# LEFT #######################################################
        self.Frameleft = Frame(self.master, width=500, bg='#CAE1FF')
        self.Frameleft.pack(side=LEFT, fill=Y)
        #############################################################################################
        self.Groupe = Label(self.Frameleft,text='Groupe', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Groupe.place(x=10,y=20, width=100, height=40)
        self.Classroom = Label(self.Frameleft,text='Classroom', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Classroom.place(x=10,y=70, width=100, height=40)
        self.Proffesseur = Label(self.Frameleft,text='Proffesseur', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Proffesseur.place(x=10,y=120, width=100, height=40)
        self.Date = Label(self.Frameleft,text='Date', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Date.place(x=10,y=170, width=100, height=40)
        self.Time = Label(self.Frameleft,text='Time', fg='#4F4F4F', bg='#CAE1FF', font=('tahoma',12,'bold'))
        self.Time.place(x=10,y=220, width=100, height=40)
        self.gp = StringVar()
        self.clasm = StringVar()
        self.prof = StringVar()
        self.dat = StringVar()
        self.tim = StringVar()
##################################

    


    
########################################################
        self.Groupe = Entry(self.Frameleft,text='Groupe', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.gp)
        self.Groupe.config(justify="center")
        self.Groupe.place(x=120,y=20, width=200, height=40)
        self.Classroom = Entry(self.Frameleft,text='Classroom', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.clasm)
        self.Classroom.config(justify="center")
        self.Classroom.place(x=120,y=70, width=200, height=40)
        self.Proffesseur = Entry(self.Frameleft,text='Proffesseur', fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), textvariable = self.prof)
        self.Proffesseur.config(justify="center")
        self.Proffesseur.place(x=120,y=120, width=200, height=40)
        self.Date = DateEntry(self.Frameleft, text='Date', width=12, fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), background='#6E7B8B', foreground='white', borderwidth=2, state = 'readonly', date_pattern='dd/mm/yyyy', textvariable = self.dat)
        self.Date.config(justify="center")
        self.Date.place(x=120,y=170, width=200, height=40)
        self.Time = ttk.Combobox(self.Frameleft,text='Time', values=["","9:00 AM", "10:30 AM", "12:00 PM", "1:30 PM", "3:00 PM", ], state = 'readonly', font=('tahoma',12,'bold'), textvariable = self.tim)
        self.Time.config(justify="center")
        self.Time.place(x=120,y=220, width=200, height=40)

###########################################################################
        
        def on_focus_in(event):
         event.widget.config(fg='black', bg="#B0E2FF")
        def on_focus_out(event):
         event.widget.config(fg='#4F4F4F', bg="white") 

        self.Groupe.bind("<FocusIn>", on_focus_in)
        self.Groupe.bind("<FocusOut>", on_focus_out)
        self.Classroom.bind("<FocusIn>", on_focus_in)
        self.Classroom.bind("<FocusOut>", on_focus_out)
        self.Proffesseur.bind("<FocusIn>", on_focus_in)
        self.Proffesseur.bind("<FocusOut>", on_focus_out)
        

###############################################################################           

        self.buttonAdd=Button(self.Frameleft,text='Add', command=self.add, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonAdd.place(x=20,y=300, width=60, height=60)
        self.buttonUp=Button(self.Frameleft,text='Update', command=self.update, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonUp.place(x=100,y=300, width=60, height=60)
        self.buttonDel=Button(self.Frameleft,text='Delete', command=self.delete, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonDel.place(x=180,y=300, width=60, height=60)
        self.buttonRead=Button(self.Frameleft,text='Show', command=self.read, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonRead.place(x=260,y=300, width=60, height=60)
        self.buttonReset=Button(self.Frameleft,text='Reset', command=self.reset, bg='#6E7B8B', fg='white', font=('tahoma',10,'bold'))
        self.buttonReset.place(x=340,y=300, width=60, height=60)
    

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
        

        self.table = ttk.Treeview(self.frameView, column= ("ID","Groupe","Classroom","Professeur","Date","Time"), show='headings', yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview())       
        self.table.pack(fill=BOTH)
         


        self.table.heading("ID",text="ID")
        self.table.heading("Groupe",text="Groupe")
        self.table.heading("Classroom",text="Classroom")
        self.table.heading("Professeur",text="Professeur")
        self.table.heading("Date",text="Date")
        self.table.heading("Time",text="Time")

        self.table.column("ID", anchor=W, width=5)
        self.table.column("Groupe", anchor=W, width=6)
        self.table.column("Classroom", anchor=W, width=6)
        self.table.column("Professeur", anchor=W, width=6)
        self.table.column("Date", anchor=W, width=6)
        self.table.column("Time", anchor=W, width=6)

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
        req = " insert into exam(Groupe, Classroom, Proffesseur, Date, Time) values (%s, %s, %s, %s, %s) "
        if (self.Groupe.get() == '' or self.Classroom.get() == '' or self.Proffesseur.get() == '' or self.Date.get() == '' or self.Time.get() == '') :
          mb.showerror('Error','Complete all the blanks', parent=self.master)
          
     #   else :
     #       if ( not self.Groupe.get().isalpha()  or not self.Classroom.get().isalpha() or not self.Proffesseur.get().isdigit() or not self.Date.get().isalpha() or not self.Time.get().isdigit() ) :
     #         mb.showerror('Error','Give us the true information', parent=self.master) 

        else :  
              val = (self.Groupe.get(), self.Classroom.get(), self.Proffesseur.get(), self.Date.get(), self.Time.get())          
              mycursor.execute(req, val)        
              mydb.commit()
              mydb.close() 
              mb.showinfo('Successfuly added','Data inserted Successfuly', parent=self.master)
              self.read()

              self.Groupe.delete(0,'end')
              self.Classroom.delete(0,'end')
              self.Proffesseur.delete(0,'end')
              self.Time.delete(0,'end') 


    def read(self):  
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = " select * from exam "
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
        self.gp.set(val[1])
        self.clasm.set(val[2])
        self.prof.set(val[3])
        self.dat.set(val[4])
        self.tim.set(val[5])


    def reset(self):
        self.Groupe.delete(0,'end')
        self.Classroom.delete(0,'end')
        self.Proffesseur.delete(0,'end')
        self.Time.delete(0,'end')   
       
    def delete(self):
        mydb = mc.connect(
          host = 'localhost',
          user = 'root',
          password = '',
          database = 'university',
          charset= 'utf8mb4'
        )
        mycursor = mydb.cursor()
        req = ("delete from exam where ID="+self.data)
        mycursor.execute(req)
        mydb.commit()
        mydb.close()
        mb.showinfo('Delete', 'The exam was deleted', parent=self.master)
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

        if (self.gp.get() == '' or self.clasm.get() == '' or self.prof.get() == '' or self.dat.get() == '' or self.tim.get() == '') :
          mb.showerror('Error','Complete all the blanks', parent=self.master)
          
#        else :
#            if ( not self.first.get().isalpha()  or not self.last.get().isalpha() or not self.matr.get().isdigit() or not self.mail.get().isalpha() or not self.ph.get().isdigit() ) :
#              mb.showerror('Error','Give us the true information', parent=self.master)         
         
        else:

              req = ("update exam set Groupe=%s, Classroom=%s, Proffesseur=%s, Date=%s, Time=%s where ID=%s ")
              val = (self.gp.get(), self.clasm.get(), self.prof.get(), self.dat.get(), self.tim.get(), self.data)
              mycursor.execute(req, val)
              mydb.commit()
              mydb.close()
              mb.showinfo('Update', 'The exam was updated', parent=self.master)
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
        req = (" select * from exam where ID="+self.studentsearch.get())
        mycursor.execute(req)
        result = mycursor.fetchone()
        if (result == None) :
           mb.showerror('Error','The exam not exist', parent=self.master) 
           print(result)  
                
        else  :
          
          print(result)
          self.table.delete(*self.table.get_children()) 
          self.table.insert('','end', iid=result[0], values=result)
          mydb.commit()
          mydb.close() 
          
