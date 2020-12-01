class user_interface:
    
    import tkinter as tk
    import os
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
    if (os.stat("data.txt").st_size == 0):
        
        location_Window = tk.Toplevel(tkWindow)  
        location_Window.geometry('200x80')  
        location_Window.title('Location Request')
        tkWindow.eval(f'tk::PlaceWindow {str(location_Window)} center')
        
        Label = tk.Label(location_Window, text="Please enter your Location:").grid(row=0, columnspan=2)
        # get country
        user_country_Label = tk.Label(location_Window, text="Country:").grid(row=1, column=0)
        user_country = tk.StringVar()
        user_country_Entry = tk.Entry(location_Window, textvariable=user_country).grid(row=1, column=1, sticky='W') 
        # get zip code
        user_zip_Label = tk.Label(location_Window, text="ZIP-Code:").grid(row=2, column=0)
        user_zip = tk.StringVar()
        user_zip_Entry = tk.Entry(location_Window, textvariable=user_zip).grid(row=2, column=1, sticky='W')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    tkWindow.mainloop()
        
                
                
                





