import tkinter as tk
from functools import partial
import os
from tkinter.messagebox import showinfo

    

def validate_Login(username, password):
    username = username.get()
    password = password.get()
    
    # incomplete login
    if ((not username) | (not password)):
        showinfo("Window", "Please type in Username and Password")
        return
    
    # new user
    if (new_acc.get() == 1):
                
             
        dir = "accounts//" + username + "_account"    
        dir_exists = os.path.isdir(dir) 
        
        # user already exists
        if (dir_exists):
                    showinfo("Window", "Username taken")
        
           
        else: 
            os.mkdir(dir)
            
            new_dir = dir + "//" + username                           
            
            # write key and encrypted password
            with open(new_dir + "_login.txt", "w") as file:
                file.write(password)
            
            # make txt files for later use  
            with open(new_dir + "_diary.txt", "w") as file:
                pass
            with open(new_dir + "_tasks.txt", "w") as file:
                pass
            with open(new_dir + "_field.txt", "w") as file:
                pass
            # open user interface and continue
            tkWindow.destroy()
            
            from user_interface import User_interface
            User_interface(username)
            
                    
    # user login   
    else:
        my_file = "accounts/" + username + "_account/" + username + "_login.txt"
        # wrong username
        if (not os.path.isfile(my_file)):
            showinfo("Window", "User doesn't exist")
        
        # username exists -> check password   
        else:
            with open(my_file) as myFile:
                check_pw = myFile.read()
                 
                if (check_pw == password):
                    tkWindow.destroy()
                    from user_interface import User_interface
                    User_interface(username)
                    

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

validateLogin = partial(validate_Login, username, password)

#login button
loginButton = tk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0) 
new_acc = tk.IntVar()
tk.Checkbutton(tkWindow, text="New Account", variable=new_acc).grid(row=4, column=1, sticky=tk.W) 

# center screen
from center_window import Center_window
cw = Center_window()
cw.place_window(200, 80, tkWindow)

    

tkWindow.mainloop()




