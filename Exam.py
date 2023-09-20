from tkinter import *
from PIL import Image,ImageTk

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
        self.master = Toplevel()
        self.master.title('Exam Managment System')