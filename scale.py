import tkinter as tk
window=tk.Tk()
window.title('Scale exercise')
window.geometry('300x200')

l=tk.Label(window, bg='yellow',width=20,text='empty')
l.pack()

def print_selection(v):
    l.config(text='youhave selected'+v)
# v是scale当前的传入值
s=tk.Scale(window,label='try me', from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=0,tickinterval=3,resolution=0.01,command=print_selection)
s.pack()
window.mainloop()