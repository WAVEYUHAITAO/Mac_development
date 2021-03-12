#! usr/bin/env
import tkinter as tk

window=tk.Tk()
window.title('my window')
window.geometry('200x100+100+200')

var=tk.StringVar()

on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
#create a label
l=tk.Label(window,textvariable=var, bg='green', font=('Arial',12), width=15, height=2)
l.pack()
#create a button
b=tk.Button(window,text='hit me', width=15, height=2, command=hit_me)
b.pack()
window.mainloop()