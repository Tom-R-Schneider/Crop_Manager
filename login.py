import tkinter as tk
from functools import partial
import os

def validateLogin(username, password):
    username = username.get()
    password = password.get()
    
    if ((not username) | (not password)):
        print("No")
        return
    
    if (new_acc.get() == 1):
        counter = 0;
        
        # Generates a key and save it into a file

            
        from cryptography.fernet import Fernet
        
        key = Fernet.generate_key()
                
        # encrypts password
        encoded_password = password.encode()
        f = Fernet(key)
        encrypted_password = f.encrypt(encoded_password)
        
        
     
            
        file_exists = os.path.isfile("accounts//" + username + "_data.txt") 
        
        if (file_exists):
            print("Username Taken")
           
        else: 
               
            f = open("accounts//" + username + "_data.txt", "w")
            f.write("Username: " +username + "\nkey: " + str(key) + "\npassword: " + str(encrypted_password))
            f.close()
            
            
        

        
        
        
        
        
    else:
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




