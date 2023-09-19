from tkinter import *
from PIL import Image,ImageTk

class Library:
    def __init__(self,bottomFrame):
        self.bottom = bottomFrame
        self.libraryFrame = Frame(self.bottom, pady=5,padx=5)
        self.libraryFrame.grid(row=1,column=0, sticky='senw')    
        self.img4 = Image.open('C:\\Users\\pc\\Student système managment\\images\\open-book.png')
        self.img4.thumbnail((180,180))
        self.new_img4 = ImageTk.PhotoImage(self.img4)
        self.imgLibrary = Label(self.libraryFrame, image = self.new_img4, pady=5, padx=5)
        self.imgLibrary.pack()
        self.buttonLibrary = Button(self.libraryFrame, text='About Library',command=self.OpenWindowLibrary, bg='#1b9ea4', fg='white', padx=5, pady=5,font=('tahoma') )
        self.buttonLibrary.pack()

    def OpenWindowLibrary(self):
        self.master = Toplevel()
        self.master.title('Library Managment System')