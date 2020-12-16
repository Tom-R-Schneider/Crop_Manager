class Weather:
    # https://www.freecodecamp.org/news/obtain-historical-weather-forecast-data-in-csv-format-using-python/ 
    def get_weather_data(self, name, x, y):
        
        # Weather Download via worldweatheronline.com (wwo_hist by Ekapope Viriyakovithya (ekapope.github.io/))
        from wwo_hist import retrieve_hist_data
        import os
        import urllib.request
                
        os.chdir(".\locations")
        
        FREQUENCY = 24
        START_DATE = '01-JAN-2010'
        END_DATE = '31-DEC-2019'
        API_KEY = '6ad530555d2e4309bda205906201412'
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
        
        os.rename(".\\" + ",".join(LOCATION_LIST) + ".csv", ".\\" + name + ".csv")