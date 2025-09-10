import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

import test



root = tb.Window(themename="darkly")

def mula():
    dif.place(relx=0.5,rely=0.2,anchor=CENTER)
    hard_but.place(relx=0.35,rely=0.3,anchor=CENTER)
    easy_but.place(relx=0.65,rely=0.3,anchor=CENTER)
    strt_but.place_forget()
    

def letsgo_H():
    dif.config(text="Ayuh mulakan")
    label.place_forget()
    hard_but.place_forget()
    easy_but.place_forget()
    user.pack()
    enter_but.pack()
    g1.place(relx=0.25,rely=0.5,anchor=CENTER)
    g2.place(relx=0.35,rely=0.5,anchor=CENTER)
    g3.place(relx=0.45,rely=0.5,anchor=CENTER)
    g4.place(relx=0.55,rely=0.5,anchor=CENTER)
    g5.place(relx=0.65,rely=0.5,anchor=CENTER)
    g6.place(relx=0.75,rely=0.5,anchor=CENTER)
    
       

def letsgo_E():
    dif.config(text="Letsgoo")
    label.place_forget()
    hard_but.place_forget()
    easy_but.place_forget()
    user.pack()
    enter_but.pack()
    
    g1.place(relx=0.35,rely=0.5,anchor=CENTER)
    g2.place(relx=0.45,rely=0.5,anchor=CENTER)
    g3.place(relx=0.55,rely=0.5,anchor=CENTER)
    g4.place(relx=0.65,rely=0.5,anchor=CENTER)
    
   
    
    
def start():
    data= user.get()
    mama = list(data)
    Label_def = tb.Label(text="Enter the correct amount of word ")
    if len(mama) == 6 or len(mama)==4:
        g1.config(text=mama[0])
        g2.config(text=mama[1])
        g3.config(text=mama[2])
        g4.config(text=mama[3])
        g5.config(text=mama[4])
        g6.config(text=mama[5])
    else:
        Label_def.place(relx=0.5,rely=0.3,anchor=CENTER)
    
    


user  = tb.Entry(root)



g1 = tb.Label(root,text= "", background="grey", font=("Roboto", 28), width=5, relief="raised") 
g2 = tb.Label(root,text= "", background="grey", font=("Roboto", 28), width=5, relief="raised") 
g3 = tb.Label(root,text= "", background="grey", font=("Roboto", 28), width=5, relief="raised") 
g4 = tb.Label(root,text= "", background="grey", font=("Roboto", 28), width=5, relief="raised") 
g5 = tb.Label(root,text= "", background="grey", font=("Roboto", 28), width=5, relief="raised") 
g6 = tb.Label(root,text= "", background="grey", font=("Roboto", 28), width=5, relief="raised") 



style_sheet= tb.Style()
style_sheet.configure('hard.TButton',font=("Robotic",20))

strt_but = tb.Button(bootstyle="info, outline",
                     text="Start",
                     width=15,
                     style="hard.TButton",
                     command=mula)
strt_but.place(relx=0.5,rely=0.5,anchor=CENTER)

root.title("Lexiqon_Quest")

label = tb.Label(root,text="Welcome to Lexiqon Quest!",
                 font=("Robotic",40))
label.place(relx=0.5,rely=0.1,anchor=CENTER)


dif = tb.Label(root,text="Choose Your Difficulty ",
               font=("Robotic",30))


hard_but = tb.Button(bootstyle="info, outline",
                     text="Hard",
                     width=15,
                     style="hard.TButton",
                     command=letsgo_H)


easy_but = tb.Button(bootstyle="info, outline",
                     text="Easy",
                     style="hard.TButton",
                     width=15,
                     command=letsgo_E)                


enter_but= tb.Button(bootstyle="info, outline",
                     text="Click me!",
                     style="hard.TButton",
                     width=15,
                     command=start)






root.geometry('800x800')
root.mainloop()





