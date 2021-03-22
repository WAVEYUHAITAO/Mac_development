import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('辅助')
window.geometry('450x300')

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(30, 20, anchor='nw', image=image_file)
canvas.pack(side='top')

tk.Label(window, text='user name:').place(x=60, y=210)
tk.Label(window, text='password:').place(x=60, y=230)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=210)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=230)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except EOFError:
        return None
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)  # pickle.dump 以二进制存入信息
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome', message='How are u ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong,try again')
    else:
        is_sign_up = tk.messagebox.askyesno(message='welcome,you have not sign up yet.Sign up today?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    usr_name = tk.StringVar()
    usr_pwd = tk.StringVar()
    confirm_pwd = tk.StringVar()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('Sign Up')
    window_sign_up.geometry('300x200')
    tk.Label(window_sign_up, text='user name:').place(x=30, y=30)
    tk.Label(window_sign_up, text='password :').place(x=30, y=70)
    tk.Label(window_sign_up, text='Confirm  :').place(x=30, y=110)
    tk.Entry(window_sign_up, textvariable=usr_name).place(x=110, y=30)
    tk.Entry(window_sign_up, textvariable=usr_pwd).place(x=110, y=70)
    tk.Entry(window_sign_up, textvariable=confirm_pwd).place(x=110, y=110)

    def sign_up_reset():
        usr_name.set('')
        usr_pwd.set('')
        confirm_pwd.set('')

    def sign_up_check():
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except EOFError:
            return None
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)  # pickle.dump 以二进制存入信息
        if usr_name.get() in usrs_info:
            tk.messagebox.showinfo(title='Sign up', message='user name already exist, pls change')

        else:
            if usr_pwd.get() == '' or confirm_pwd.get() == '':
                tk.messagebox.showwarning(title='Sign up', message='pls input password and double confirm')
            else:
                if usr_pwd.get() != confirm_pwd.get():
                    tk.messagebox.showerror(title='Sign up', message='两次输入的密码不一致，请重新输入')
                else:

                    usr_file = open('usrs_info.pickle', 'wb')
                    usrs_info[usr_name.get()] = usr_pwd.get()  # 将用户注册的账号密码保存入usrs_info
                    pickle.dump(usrs_info, usr_file)  # 把用户输入保存入pickle file
                    usr_file.close()
                    tk.messagebox.showinfo(message='congratulations, you have successfully sign up')

    tk.Button(window_sign_up, text='ok', width=7, command=sign_up_check).place(x=70, y=145)
    tk.Button(window_sign_up, text='cancel', width=7, command=window_sign_up.destroy).place(x=140, y=145)
    tk.Button(window_sign_up, text='reset', command=sign_up_reset).place(x=210, y=145)


btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=260)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=220, y=260)

window.mainloop()
