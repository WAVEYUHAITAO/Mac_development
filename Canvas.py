import tkinter as tk
window=tk.Tk()
window.title('canvas')
window.geometry('1000x800')

canvas=tk.Canvas(window,bg='blue',height=500,width=700)
image_file=tk.PhotoImage(file='DSC02016.PNG') #此版本tkinter只能加载png格式图片
image=canvas.create_image(0,0,anchor='nw',image=image_file)
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1) 
oval=canvas.create_oval(x0,y0,x1,y1,fill='red') #x0,y0,x1,y1为圆外矩形左上和右下坐标
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=45,extent=180,fill='red')
rect=canvas.create_rectangle(100,30,100+20,30+20)
canvas.pack()


def moveit():
    canvas.move(rect,0,2)
    canvas.move(oval,0,2)
b=tk.Button(window,text='move',command=moveit)
b.pack()


window.mainloop()