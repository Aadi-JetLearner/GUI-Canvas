from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
F = False
X = False
wd = Tk()
wd.geometry("550x550")
wd.config(background="white")
wd.title("CANVAS")
Z = "black"
Width = 0
S_X = None
S_Y = None
def Colour_Palette():
    Raise_Button(BT3)
    global Z
    Z = askcolor(Z)[1]
    

def Eraser():
    Raise_Button(BT4)
    global F
    F =  True

    

def Write_Pen():
    Raise_Button(BT1)
    global X
    X = True


def Write_Brush():
    Raise_Button(BT2)
    S.set(50)

def Erase_All():
    Raise_Button(BT5)
    C.delete("all")
def Draw_Pen(event):
    global X
    global S_X, S_Y
    global Width
    Width = S.get()
    if Width >= 20 and X == True:

        messagebox.showwarning("showinfo", "Please use Brush Tool to access widths more than this. ")
        Write_Brush()
        X = False

    if S_X and S_Y:
        if F == True:
            global Z
            Z = "white"
        
        C.create_line(S_X, S_Y, event.x, event.y, width = Width, fill = Z, capstyle = ROUND, smooth = TRUE)
    S_X = event.x
    S_Y = event.y
BT1 = Button(wd, bg = "grey", width = 8, height = 2, text = "Pen",command = Write_Pen)
BT1.grid(row = 1, column = 0)
BT2 = Button(wd, bg = "grey", width = 8, height = 2, text = "Brush",command = Write_Brush)
BT2.grid(row = 1, column = 1)
BT3 = Button(wd, bg = "grey", width = 8, height = 2, text = "Colour",command = Colour_Palette)
BT3.grid(row = 1, column = 2)
BT4 = Button(wd, bg = "grey", width = 8, height = 2, text = "Erase",command = Eraser)
BT4.grid(row = 1, column = 3)
BT5 = Button(wd, bg = "grey", width = 8, height = 2, text = "Erase All",command = Erase_All)
BT5.grid(row = 1, column = 4)


C = Canvas(wd, bg = "white", width = 550, height = 500)
C.grid(row = 2, column = 0, columnspan = 8)
C.bind("<B1-Motion>", Draw_Pen)
S = Scale(wd, bg ="white", from_= 1,to=50, orient = HORIZONTAL)
S.grid(row = 1, column = 7)

AC = BT1
def Raise_Button(AB):
    global F
    global AC
    AC.config(relief=RAISED)
    AB.config(relief = SUNKEN)
    AC = AB
    F = False


































#











































wd.mainloop()