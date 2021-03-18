import tkinter as tk
window=tk.Tk()
window.title('Checkbutton exercise')
window.geometry('300x200')

l=tk.Label(window,bg='yellow',text='empty',width=20)
l.pack()

def print_selection():
    if(var1.get()==1)&(var2.get()==0):
        l.config(text='I love Python only')
    elif(var1.get()==0)&(var2.get()==1):
        l.config(text='I love C++ only')
    elif(var1.get()==1)&(var2.get()==1):
        l.config(text='I love both')
    else:
        l.config(text='I love neither')
#check box
var1=tk.IntVar()
var2=tk.IntVar()
c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_selection)
c2=tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()
t=tk.Text(window,height=2)
t.pack()
t.insert('insert',c1) #to see what is returned by c1
window.mainloop()