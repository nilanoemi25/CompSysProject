from sense_hat import SenseHat
import time
from datetime import datetime

def get_employee_data(deviceID):
    # Initialize SenseHAT
    sense = SenseHat()
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    flag="default"
    if humidity > 15 and temp < 35:
     flag = "It's probably raining today.Employees may be late due to adverse weather conditions."
    else:
     flag = "The weather looks good today. Employees have no excuse to be late."

    #Lets say that Sherlock starts at 9 am, James at 10 am, John at 11am and Irene at 12 noon
    current_time = datetime.now()
    current_time_pretty = f"Photo taken at {current_time:%H:%M}"
    photo_published = True
    is_ontime = True
    seconds = time.time()
    result = time.localtime(seconds) 
    if result.tm_hour >= 9 and result.tm_hour < 10:
         employee="Sherlock Holmes"
         employeeId="1111"
    elif result.tm_hour >= 10 and result.tm_hour < 11:
        employee="James Moriarty"
        employeeId="1112"
    elif result.tm_hour >= 11 and result.tm_hour < 12:
        employee="John H Watson"
        employeeId="1113"
    elif result.tm_hour >= 12 and result.tm_hour < 13:
        employee="Irene Adler"
        employeeId="1114"
    elif result.tm_hour >= 13 and result.tm_hour < 14:
        employee="Mary Morstan"
        employeeId="1115"       
    elif result.tm_hour >= 14 and result.tm_hour < 15:
        employee="Mycroft Holmes"
        employeeId="1116"     
    elif result.tm_hour >= 15 and result.tm_hour < 16:
        employee="Detective Lestrade"
        employeeId="1117"     
    elif result.tm_hour >= 17 and result.tm_hour < 18:
        employee="Mrs Hudson"
        employeeId="1118"  
    elif result.tm_hour >= 18 and result.tm_hour < 19:
        employee="Molly hooper"
        employeeId="1119"                           
    else:
        employee="Could be anyone"
        employeeId="9999"

    if result.tm_min > 5 and result.tm_min < 59 and result.tm_min != 0:
        is_ontime = False 
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "temp": round(temp,2),
        "humidity": round(humidity,2),
        "employee": employee,
        "employeeId": employeeId,
        "weather_condition": flag,
        "time_keeping": is_ontime,
        "current_time": current_time_pretty,
        "photo_published": photo_published 
        
    }
    
    return data