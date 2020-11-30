class user_interface:
    import tkinter as tk
    from tkinter import font as tkFont
    from functools import partial
    import matplotlib.pylab as plt
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    
    #window
    tkWindow = tk.Tk()  
    tkWindow.geometry('1600x900')  
    tkWindow.title('Schneider Crop Manager')
    tkWindow.resizable(True, True)
    
    my_font = tkFont.Font(family='Helvetica', size=36)
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    
    input_frame = tk.Frame(tkWindow, width = 1600, height = 700, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame.pack(side = tk.TOP, anchor=tk.NW)

    button1=tk.Button(tkWindow, text="Temperature", height = 195, width = 395, font = my_font, image=pixelVirtual)
    button1.place(x=400, y=700)
    
    button2=tk.Button(tkWindow, text="Calender", height = 195, width = 395, font = my_font, image=pixelVirtual)
    button2.place(x=800, y=700)
    
    button3=tk.Button(tkWindow, text="Notes", height = 195, width = 395, font = my_font, image=pixelVirtual)
    button3.place(x=1200, y=700)
    
    tkWindow.mainloop()