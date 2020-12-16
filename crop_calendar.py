class Crop_calendar:
    
    import calendar
    import datetime
    
    c = calendar.TextCalendar(calendar.THURSDAY)
    str = c.formatmonth(2025, 1, 0, 0)
    print(str)
        
    x = datetime.datetime.now()
    print(x.strftime("%d %B %Y \n%A"))
    
    from weather import Weather
    Weather.get_weather_data(Weather,"heidelberg", "49.402", "8.676")