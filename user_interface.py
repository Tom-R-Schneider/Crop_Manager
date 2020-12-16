class User_interface:
    
    def __init__(self, username):
        
        import tkinter as tk
        import os
        
        self.username = username
        #window
        tkWindow = tk.Tk()  
        tkWindow.geometry('1600x900')  
        tkWindow.title('Schneider Crop Manager')
        tkWindow.resizable(True, True)
        
        screen_width = tkWindow.winfo_screenwidth()
        screen_height = tkWindow.winfo_screenheight()
        
        window_width = 1600
        window_height = 900
        
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        
        tkWindow.geometry('%dx%d+%d+%d' % (window_width, window_height, x_cordinate, y_cordinate))
        
        
        # if no location is given, get location   
        file_name = "accounts//" + self.username + "_account//" + self.username + "_data.txt" 
        if (os.stat(file_name).st_size == 0):
            
            def get_Location(self):
                pass
            
            location_Window = tk.Toplevel(tkWindow)  
            location_Window.geometry('200x100')  
            location_Window.title('Location Request')
            tkWindow.eval(f'tk::PlaceWindow {str(location_Window)} center')
            
            Label = tk.Label(location_Window, text="Please enter your Location:").grid(row=0, columnspan=2)
            # get name
            user_country_Label = tk.Label(location_Window, text="City Name:").grid(row=1, column=0)
            user_country = tk.StringVar()
            user_country_Entry = tk.Entry(location_Window, textvariable=user_country).grid(row=1, column=1, sticky='W') 
            # get x coordinate
            user_x_Label = tk.Label(location_Window, text="Longitude:").grid(row=2, column=0)
            user_x = tk.StringVar()
            user_x_Entry = tk.Entry(location_Window, textvariable=user_x).grid(row=2, column=1, sticky='W')
            # get y coordinate
            user_y_Label = tk.Label(location_Window, text="Latitude:").grid(row=3, column=0)
            user_y = tk.StringVar()
            user_y_Entry = tk.Entry(location_Window, textvariable=user_x).grid(row=3, column=1, sticky='W')
            
            loginButton = tk.Button(location_Window, text="Get Location Data", command=get_Location).grid(row=4, column=0, columnspan = 2) 
            new_acc = tk.IntVar()
    
    
    
   
    
    
    
        
            tkWindow.mainloop()
        
                
                
                





