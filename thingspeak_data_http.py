from sense_hat import SenseHat
import requests
import time
from employee_data import get_employee_data

sense = SenseHat()

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "YQ2PNEN438H27L0G"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature,humidity,is_ontime,employeeId):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature,
        'field2': humidity,
        'field3': is_ontime,
        'field4': employeeId,
    
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   


while True:
    # Read temperature and humidity from Sense HAT
    temperature = round(sense.get_temperature(),2)
    humidity=round(sense.humidity,2)
    is_ontime = True
    seconds = time.time()
    result = time.localtime(seconds) 
    if result.tm_min > 2 and result.tm_min < 45 and result.tm_min != 0:
        is_ontime = False 

    deviceId= "anydevice"
    data = get_employee_data(deviceId)
    employeeId = data['employeeId']
    
    print(f"Temperature: {temperature} C")
    print(f"Humidity: {humidity} ")
    print(f"Time Keeping: {is_ontime} ")
    print(f"EmpId: {employeeId} ")
    
   

    # Send the data to ThingSpeak
    send_to_thingspeak(temperature,humidity,is_ontime,employeeId)

    # Wait before the next reading (ThingSpeak recommends 15-second intervals for free accounts)
    time.sleep(16)
