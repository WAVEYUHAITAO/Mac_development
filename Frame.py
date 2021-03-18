import tkinter as tk
window=tk.Tk()
window.title('frame exercise')
window.geometry('300x200')

tk.Label(window,text='on the window').pack()

frm=tk.Frame(window)
frm.pack()
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l,text='on the frm_l 1').pack()
tk.Label(frm_l,text='on the frm_l 2').pack()
tk.Label(frm_r,text='on the frm_r 1').pack()
window.mainloop()
