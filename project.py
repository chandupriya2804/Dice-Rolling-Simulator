from tkinter import *
import random

root=Tk()
root.geometry("700x450")
root.title("Roll Dice")


label=Label(root,text="",font=("times",260))

def roll():
    dice= ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()


button = Button(root,text="Lets Roll...",command=roll)
button.place(x=300,y=0)

root.mainloop()
