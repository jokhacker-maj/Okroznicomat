#Import the required libraries
from tkinter import *
from tkinter import ttk
import chat
import email_reader

#Create an instance of Tkinter Frame
win = Tk()

win.title("Okroznicomat")

#Set the geometry of Tkinter Frame
win.geometry("500x200")

   

def povzetek():
    posta = email_reader.get_messages()
    besedilo = chat.povzetek(posta , 1)
    T = Text(Tk(), height=20, width=100)
    T.insert(END,besedilo)
    T.pack()

def povzetka():
    posta = email_reader.get_messages()
    besedilo = chat.povzetek(posta , 2)
    T = Text(Tk(), height=20, width=100)
    T.insert(END,besedilo)
    T.pack()
    
def povzetki():
    posta = email_reader.get_messages()
    besedilo = chat.povzetek(posta , 5)
    T = Text(Tk(), height=20, width=100)
    T.insert(END,besedilo)
    T.pack()




#Create a Label widget
Label(win, text= "Program napiše povzetek okrožnic").pack(pady=15)

ttk.Button(win, text= "Povzetek zadnje okrožnice", command=povzetek).pack()

ttk.Button(win, text= "Povzetek zadnjih 2 okrožnic", command=povzetka).pack()

ttk.Button(win, text= "Povzetek zadnjih 5 okrožnic", command=povzetki).pack()

#ttk.Button(win, text= "Vse okrožnice", command=povzetek).pack()

ttk.Button(win, text = "Izhod iz programa", command = win.destroy).pack() 



win.mainloop()