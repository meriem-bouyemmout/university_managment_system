from tkinter import *
import tkinter as tk
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
        stdw = infoWindow() 

class infoWindow :
    def __init__(self):
        self.master = Toplevel()
        self.master.iconbitmap('C:\\Users\\pc\\Student système managment\\images\\swim_ring_icon_183313.ico')
        self.master.title('About University')
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
####################################################################################
        self.titleLabel = Label(self.master, text="Faculty des sciences Alger 1", bg='#1b9ea4', fg='white', pady=50, font=('tahoma',40,'bold') ) 
        self.titleLabel.pack(fill=X, pady=30)  
        self.text = StringVar()       
        self.Message = Message(self.master, textvariable=self.text, justify=CENTER, font=('tahoma', '15'))
        self.Message.pack()
        self.text.set("UN PÔLE UNIVERSITAIRE D’EXCELLENCE À L’UNIVERSITÉ BENYOUCEF BENKHEDDA LA FACULTÉ DES SCIENCES\n La Faculté des Sciences créée en juillet 2015, est l’un des quatre établissements de l’Université d’Alger 1. Cette dernière s’étend sur un vaste territoire composé de plusieurs structures :\n   Le bloc principal domicilié à l’ex fac centrale et qui abrite ;\n Le Rectorat et les vices rectorat et les services centraux,\n   Décanat de la Faculté des Sciences (FS),\n   La Bibliothèque Centrale (BU),\n   La bibliothèque de la Faculté des Sciences\n   Le Centre des langues intensives\n   Le Centre Médico-social (CMS),\n   La Faculté de droit domiciliée à Saïd Hamdine.\n   La Faculté de Médecine domiciliée à Ben Aknoun.\n   La Faculté des Sciences islamiques domiciliée à Hussein Dey.\n")
        def open_facebook():
           import webbrowser
           webbrowser.open("https://www.univ-alger.dz/?lang=fr")

        def open_google():
           import webbrowser
           webbrowser.open("https://www.facebook.com/FaculteDesSciences2015/")
        
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(side="bottom")

        self.facebook_label = tk.Label(self.bottom_frame, text="Facebook", fg="blue", cursor="hand2")
        self.facebook_label.pack(side="left")
        self.facebook_label.bind("<Button-1>", lambda e: open_facebook())

        self.google_label = tk.Label(self.bottom_frame, text="Google", fg="blue", cursor="hand2")
        self.google_label.pack(side="right")
        self.google_label.bind("<Button-1>", lambda e: open_google())

