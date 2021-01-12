class Field:
    def __init__(self, username):
        import tkinter as tk
        from center_window import Center_window
        from datetime import datetime
        file_name = "accounts//" + username + "_account//" + username + "_field.txt"
        with open(file_name, "r") as myFile:
            count = len(myFile.readlines())
        # get field dimensions if not already given 
        if (count < 2):
            tkWindow = tk.Tk()   
            tkWindow.title('Field Dimensions')
            cw = Center_window()
            cw.place_window(200, 100, tkWindow)
            
            Label = tk.Label(tkWindow, text="Please enter your Field's Dimensions:").grid(row=0, columnspan=2)

            # get x coordinate
            dimension_Label = tk.Label(tkWindow, text="Length (m):").grid(row=1, column=0)
            dimension_x = tk.StringVar()
            dimension_x_Entry = tk.Entry(tkWindow, textvariable=dimension_x).grid(row=1, column=1, sticky='W')
            # get y coordinate
            dimension_Label = tk.Label(tkWindow, text="Width (m):").grid(row=2, column=0)
            dimension_y = tk.StringVar()
            dimension_y_Entry = tk.Entry(tkWindow, textvariable=dimension_y).grid(row=2, column=1, sticky='W')
            
            # write dimensions to field.txt as second line
            def set_dimension():
                x = dimension_x.get()
                y = dimension_y.get()
                
                with open(file_name, 'a') as file:
                    file.write("\n" + x + " " + y)    
                tkWindow.destroy()
                self.show_field(username)
            
            setButton = tk.Button(tkWindow, text="OK", command=set_dimension).grid(row=3, column=0, columnspan=2)
            tkWindow.mainloop()
            
        else:
            self.show_field(username)
            
        
    def show_field(self, username):
        import tkinter as tk
        from center_window import Center_window
        from datetime import datetime
        
        file_name = "accounts//" + username + "_account//" + username + "_field.txt"         

        with open(file_name, "r") as myFile:
            location = myFile.readline().capitalize().rstrip() 
            dimensions = myFile.readline() 
        xy_list = dimensions.split()
        x = xy_list[0].rstrip()
        y = xy_list[1].rstrip()
        area = str(int(float(x) * float(y)))
        window = tk.Tk()   
        window.title('Field Data')
        year_list = range(2021, 2050, 1)
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        variable_month = tk.StringVar(window)
        variable_year = tk.StringVar(window)
        today = datetime.today()
        variable_month.set(month_list[today.month - 1]) # default value
        variable_year.set(today.year) # default value
        year_options = tk.OptionMenu(window, variable_year, *year_list).grid(row=0, column=0)
        month_options = tk.OptionMenu(window, variable_month, *month_list).grid(row=0, column=1)
        date_Label = tk.Label(window, text="Current date: " + "{0:0=2d}".format(today.day) + "." + "{0:0=2d}".format(today.month) + "." + str(today.year)).grid(row=0, column=2)
        location_Label = tk.Label(window, text="Location: " + location).grid(row=0, column=3)
        area_Label = tk.Label(window, text="Area: {}m\u00b2".format(area)).grid(row=1, column=0)
        x_Label = tk.Label(window, text="Length: " + x + "m").grid(row=1, column=1)
        y_Label = tk.Label(window, text="Width: " + y + "m").grid(row=1, column=2)
        area_Label = tk.Label(window, text="Currently planted").grid(row=2, columnspan=4)
        h = tk.Scrollbar(window)
        t = tk.Text(window, height = 15, wrap = tk.NONE, yscrollcommand = h.set, state='disabled').grid(row=3,columnspan=4) 
        area_Label = tk.Label(window, text="Planted this month").grid(row=4, columnspan=4)
        m = tk.Scrollbar(window)
        t = tk.Text(window, height = 15, wrap = tk.NONE, yscrollcommand = m.set, state='disabled').grid(row=5,columnspan=4) 

        
        
        
        
        
        
        window.mainloop()  
        
        
        
        
        
        
        
        
        
        
                