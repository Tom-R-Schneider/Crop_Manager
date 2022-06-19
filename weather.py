class Weather:
    
    def open_weather_data(self, username):
        import tkinter as tk
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
        
        window = tk.Tk()
        
        
        from datetime import datetime
        today = datetime.today()
        curr_year = str(today.year)
        last_year = str(today.year - 1)
        
        fig = plt.figure(figsize=(13, 4))
        
        import pandas
        
        file_name = "accounts//" + username + "_account//" + username + "_field.txt"
        with open(file_name) as myFile:
                location = myFile.readline()
        
        location = location.rstrip()
        df = pandas.read_csv('locations//' + location + '.csv', usecols=["date_time","maxtempC", "mintempC"])
        
        date = df["date_time"].tolist()
        max_temp = df["maxtempC"].tolist()
        min_temp = df["mintempC"].tolist()
        
        today = datetime.today()
        curr_year = str(today.year)
        last_year = str(today.year - 1)
        
        min_temp_last = []
        min_temp_curr = []
        max_temp_last = []
        max_temp_curr = []
        
        for i in range (len(date)):
            if(last_year in str(date[i])):
                min_temp_last.append(min_temp[i])
                max_temp_last.append(max_temp[i])
            elif(curr_year in str(date[i])):
                min_temp_curr.append(min_temp[i])
                max_temp_curr.append(max_temp[i])  
        
        plt.plot(min_temp_last)
        plt.plot(min_temp_curr)
        
        plt.xlabel('Days')
        plt.ylabel('Temperatur in Celsius')
        plt.title('Minimum Temperature')
        
        
        # specify the window as master
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, ipadx=40, ipady=20)
        
        
        #max temp plot
        fig2 = plt.figure(figsize=(13, 4))
        plt.plot(max_temp_last)
        plt.plot(max_temp_curr)
        
        plt.xlabel('Days')
        plt.ylabel('Temperatur in Celsius')
        plt.title('Maximum Temperature')
        
        # specify the window as master
        canvas = FigureCanvasTkAgg(fig2, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, ipadx=40, ipady=20)
        
        # get weather data on screen
        Label = tk.Label(window, text="Current date: " + "{0:0=2d}".format(today.day) + "." + "{0:0=2d}".format(today.month) + "." + str(today.year)).grid(row=2, column=0)
        Label2 = tk.Label(window, text="Current date: " + str(today.day) + "." + str(today.month) + "." + str(today.year)).grid(row=2, column=1)
        
        from center_window import Center_window
        cw = Center_window()
        cw.place_window(window.winfo_width(), window.winfo_height() * 2, window)          
        window.mainloop()
            
    
    
    # https://www.freecodecamp.org/news/obtain-historical-weather-forecast-data-in-csv-format-using-python/ 
    def get_weather_data(self, name, x, y):
        
        # Weather Download via worldweatheronline.com (wwo_hist by Ekapope Viriyakovithya (ekapope.github.io/))
        from wwo_hist import retrieve_hist_data
        from datetime import datetime
        import os
        import urllib.request
        
        # get current date for END_DATE
        from calendar import monthrange
        month_list =["JAN", "FEB", "MAR","APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        today = datetime.today()
        day = today.day - 1
        # check that no 0 is present for date
        if (day != 0):
            month = today.month
            year = today.year
        else:
            month = month - 1
            if (month != 0):
                year = today.year
                temp = monthrange(year, month)
                day = temp[1]
            else:
                day = 31
                month = 12
                year = today.year - 1
                
                
        os.chdir(".\locations")
        
        FREQUENCY = 24
        START_DATE = '01-JAN-2010'
        END_DATE = "{0:0=2d}".format(day) + "-" + month_list[month-1] + "-" + str(year) 
        API_KEY = 'API_KEY'
        LOCATION_LIST = [x + "," + y]
        name = name.lower()
        
        hist_weather_data = retrieve_hist_data(API_KEY,
                                        LOCATION_LIST,
                                        START_DATE,
                                        END_DATE,
                                        FREQUENCY,
                                        location_label = False,
                                        export_csv = True,
                                        store_df = True)
        
        print(hist_weather_data)
        
        os.rename(".\\locations\\" + ",".join(LOCATION_LIST) + ".csv", ".\\" + name + ".csv")
        os.chdir("../Schneider_Crop_Manager")
