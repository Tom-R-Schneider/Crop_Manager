import tkinter as tk
from functools import partial

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    print("New Account: ", new_acc.get())
    return

#window
tkWindow = tk.Tk()  
tkWindow.geometry('200x80')  
tkWindow.title('Schneider Crop Manager Login Window')

#username label and text entry box
usernameLabel = tk.Label(tkWindow, text="User Name").grid(row=0, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = tk.Label(tkWindow,text="Password").grid(row=1, column=0)  
password = tk.StringVar()
passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = tk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0) 
new_acc = tk.IntVar()
tk.Checkbutton(tkWindow, text="New Account", variable=new_acc).grid(row=4, column=1, sticky=tk.W) 

tkWindow.mainloop()