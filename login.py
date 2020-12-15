import tkinter as tk
from functools import partial
import os
from tkinter.messagebox import showinfo

    

def validate_Login(username, password):
    username = username.get()
    password = password.get()
    
    if ((not username) | (not password)):
        showinfo("Window", "Please type in Username and Password")
        return
    
    # new user
    if (new_acc.get() == 1):
        
        # Generates a key and save it into a file
        from cryptography.fernet import Fernet        
        key = Fernet.generate_key()
                
        # encrypts password
        encoded_password = password.encode()
        f = Fernet(key)
        encrypted_password = f.encrypt(encoded_password)
        
        
     
        dir = "accounts//" + username + "_account"    
        dir_exists = os.path.isdir(dir) 
        
        if (dir_exists):
                    showinfo("Window", "Username taken")
           
        else: 
            os.mkdir(dir)                           
            
            # write key and encrypted password
            with open(dir + "//" + username + "_login.txt", "w") as file:
                file.write("key: " + str(key) + "\npassword: " + str(encrypted_password))
            
            # make txt file for later use    
            with open(dir + "//" + username + "_data.txt", "w") as file:
                pass
            
            # open user interface and continue
            tkWindow.destroy()
            
            from user_interface import User_interface
            User_interface(username)
            
                    
    # user login   
    else:
        my_file = "accounts//" + username + "_account//" + username + "_login"
        # wrong username
        if (not os.path.isfile(my_file)):
            showinfo("Window", "Wrong Username")
        
        # username exists -> check password   
        else:
            with open(my_file) as myFile:
                key = myFile.read()
                encryp_password = myFile.read()
                 
            
            
        
        
        
        
        

        
            


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
screen_width = tkWindow.winfo_screenwidth()
screen_height = tkWindow.winfo_screenheight()

window_width = 200
window_height = 80

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

tkWindow.geometry('%dx%d+%d+%d' % (window_width, window_height, x_cordinate, y_cordinate))
    

tkWindow.mainloop()




