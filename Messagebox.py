import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title('Scale exercise')
window.geometry('300x200')

def hit_me():
    #tk.messagebox.showinfo(title='Hi',message='hahahaha')
    #tk.messagebox.showwarning(title='Hi',message='nonononono')
    #tk.messagebox.showerror(title='Hi',message='No! never')
    #print(tk.messagebox.askquestion(title='Hi',message='hahahaha'))
    print(tk.messagebox.askyesno(title='Hi',message='hahahaha'))
tk.Button(window,text='hit me',command=hit_me).pack()

window.mainloop()