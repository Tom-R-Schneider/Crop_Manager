class User_interface:
    
    def __init__(self, username):
        
        import tkinter as tk
        import os
        
            
        
      
        
        # if no location is given, get location   
        file_name = "accounts//" + username + "_account//" + username + "_field.txt" 
        if (os.stat(file_name).st_size == 0):
            
            
            #window
            tkWindow = tk.Tk()   
            tkWindow.title('Location Request')
            from center_window import Center_window
            cw = Center_window()
            cw.place_window(200, 150, tkWindow)
            


        
           
     
        
            
            Label = tk.Label(tkWindow, text="Please enter your Location:").grid(row=0, columnspan=2)
            # get name
            user_country_Label = tk.Label(tkWindow, text="City Name:").grid(row=1, column=0)
            user_country = tk.StringVar()
            user_country_Entry = tk.Entry(tkWindow, textvariable=user_country).grid(row=1, column=1, sticky='W') 
            # get x coordinate
            user_x_Label = tk.Label(tkWindow, text="Longitude:").grid(row=2, column=0)
            user_x = tk.StringVar()
            user_x_Entry = tk.Entry(tkWindow, textvariable=user_x).grid(row=2, column=1, sticky='W')
            # get y coordinate
            user_y_Label = tk.Label(tkWindow, text="Latitude:").grid(row=3, column=0)
            user_y = tk.StringVar()
            user_y_Entry = tk.Entry(tkWindow, textvariable=user_y).grid(row=3, column=1, sticky='W')
            
            def get_location():
                name = user_country.get()
                x = user_x.get()
                y = user_y.get()
                
                from weather import Weather
                hist = Weather()
                hist.get_weather_data(name, x, y)
                file_name = "accounts//" + username + "_account//" + username + "_field.txt"
                with open(file_name, "w") as file:
                    file.write(name)
                tkWindow.destroy()
            
            # confirm 
            loginButton = tk.Button(tkWindow, text="Get Location Data", command=get_location).grid(row=4, column=0, columnspan=2) 
            
            # choose location via drop down    
            def location_exist():

                tkWindow.destroy()
                tkWindow_n = tk.Tk()
                # get list of locations downloaded
                location_arr = os.listdir(".//locations//")
                location_arr = {x.replace(".csv", "") for x in location_arr}
                variable = tk.StringVar(tkWindow_n)
                variable.set("location") # default value
                
                from center_window import Center_window
                cw = Center_window()
                cw.place_window(150, 80, tkWindow_n)
                
                
                
                # drop-down menu            
                location_options = tk.OptionMenu(tkWindow_n, variable, *location_arr).grid(row=0)
    
                def set_location():
                    file_name = ".//accounts//" + username + "_account//" + username + "_field.txt" 
                    with open(file_name, "w") as file:
                        file.write(variable.get())
                    tkWindow_n.destroy()
                    
                button = tk.Button(tkWindow_n, text="OK", command=set_location).grid(row=1)
                
                tk.mainloop()
                
            # use existing location
            loginButton = tk.Button(tkWindow, text="Location already exists", command=location_exist).grid(row=5, column=0, columnspan=2) 
            
    
            tkWindow.mainloop()
            
        # menu       
        tkWindow = tk.Tk()
        tkWindow.geometry('220x258')  
        tkWindow.title('Schneider Crop Manager Menu')
        
        def open_weather():
            from weather import Weather
            ui_w = Weather()
            ui_w.open_weather_data(username) 
            
        def open_diary():
            from diary import Diary
            d = Diary(username)
        def open_field():
            from field import Field
            f = Field(username)
        
        button1 = tk.Button(tkWindow, text="Weather", command=open_weather, width=30,height=5).grid(row=0) 
        button2 = tk.Button(tkWindow, text="Diary", command=open_diary,width=30,height=5).grid(row=1) 
        button3 = tk.Button(tkWindow, text="Field", command=open_field, width=30,height=5).grid(row=2) 
        tkWindow.mainloop()
             
                





