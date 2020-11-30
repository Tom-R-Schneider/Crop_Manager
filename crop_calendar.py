class crop_calendar:
    
    import calendar
    import datetime
    
    c = calendar.TextCalendar(calendar.THURSDAY)
    str = c.formatmonth(2025, 1, 0, 0)
    print(str)
    
    
    
    x = datetime.datetime.now()
    print(x.strftime("%d %B %Y \n%A"))
    import tkinter as tk
    from functools import partial
    
    #window
    tkWindow = tk.Tk()  
    tkWindow.geometry('1500x900')  
    tkWindow.title('Schneider Crop Manager')
    tkWindow.mainloop()