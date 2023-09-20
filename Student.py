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

         self.FirstName = Entry(self.Frameleft,text='FirstName', fg='#4F4F4F', font=('tahoma',12,'bold'))
         self.FirstName.place(x=120,y=20, width=200, height=40)
         self.LastName = Entry(self.Frameleft,text='LastName', fg='#4F4F4F', font=('tahoma',12,'bold'))
         self.LastName.place(x=120,y=70, width=200, height=40)
         self.Matricule = Entry(self.Frameleft,text='Matricule', fg='#4F4F4F', font=('tahoma',12,'bold'))
         self.Matricule.place(x=120,y=120, width=200, height=40)
         self.Email = Entry(self.Frameleft,text='Email', fg='#4F4F4F', font=('tahoma',12,'bold'))
         self.Email.place(x=120,y=170, width=200, height=40)
         self.Phone = Entry(self.Frameleft,text='Phone', fg='#4F4F4F', font=('tahoma',12,'bold'))
         self.Phone.place(x=120,y=220, width=200, height=40)


         self.add=Button(self.Frameleft,text='Add', fg='#4F4F4F', font=('tahoma',10,'bold'))
         self.add.place(x=40,y=300, width=60, height=60)
         self.add=Button(self.Frameleft,text='Update', fg='#4F4F4F', font=('tahoma',10,'bold'))
         self.add.place(x=170,y=300, width=60, height=60)
         self.add=Button(self.Frameleft,text='Delete', fg='#4F4F4F', font=('tahoma',10,'bold'))
         self.add.place(x=290,y=300, width=60, height=60)




         Frameright = Frame(self.master, bg='gray', width=900)
         Frameright.pack(side=RIGHT, fill=Y)
           
    