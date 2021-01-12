class Center_window:
        def place_window(self, x, y, tkWindow):
            screen_width = tkWindow.winfo_screenwidth()
            screen_height = tkWindow.winfo_screenheight()
            
            x_cordinate = int((screen_width/2) - (x/2))
            y_cordinate = int((screen_height/2) - (y/2))
            
            tkWindow.geometry('%dx%d+%d+%d' % (x, y, x_cordinate, y_cordinate))