from sense_hat import SenseHat
import time

def get_employee_data(deviceID):
    # Initialize SenseHAT
    sense = SenseHat()
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    
    flag="default"
    if humidity > 90 and temp < 20:
     flag = "It's probably raining today.Employees may be late due to adverse weather conditions."
    else:
     flag = "The weather looks good today. Employees have no excuse to be late."

    #Lets say that Sherlock starts at 9 am, James at 10 am, John at 11am and Irene at 12 noon
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
    elif result.tm_hour >= 12 and result.tm_hour < 19:
        employee="Irene Adler"
        employeeId="1114"
    else:
        employee="Could be anyone"
        employeeId="9999"

    if result.tm_min > 2 and result.tm_min < 45 and result.tm_min != 0:
        is_ontime = False 
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "temp": round(temp,2),
        "humidity": round(humidity,2),
        "employee": employee,
        "employeeId": employeeId,
        "weather_condition": flag,
        "time_keeping": is_ontime
    }
    
    return data