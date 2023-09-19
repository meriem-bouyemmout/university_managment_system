from tkinter import *
from PIL import Image,ImageTk

class infoUniversity:

    def __init__(self,centerFrame):
        self.center = centerFrame
        self.infoUniversity = Frame(self.center, pady=5,padx=5)
        self.infoUniversity.grid(row=0,column=0, sticky='senw')    
        self.img = Image.open('C:\\Users\\pc\\Student système managment\\images\\university.png')
        self.img.thumbnail((180,180))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgUniversity = Label(self.infoUniversity, image = self.new_img, pady=5, padx=5)
        self.imgUniversity.pack()
        self.buttonUniversity = Button(self.infoUniversity, text='About University', command=self.OpenWindowUniv, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonUniversity.pack() 

    def OpenWindowUniv(self):
        self.master = Toplevel()
        self.master.title('About Univerrsity')    