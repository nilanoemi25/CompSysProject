from sense_hat import SenseHat
import sys 
sys.path.insert(0, '../')
import requests
import time
from employee_data import get_employee_data
from camera_test import capture_image
from upload_image import upload_image
import BlynkLib
import json 

with open('../udp_data.json', 'r') as file: udp_data = json.load(file)

deviceID="NoemisPi"
sense = SenseHat()
sense.clear()
IMAGE_PATH="../images/sensehat_image.jpg"
BLYNK_AUTH = 'z275UI1-xYpfjeR4JM-TroJ1R4l28_HN'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Define colours for SBC
green = (0, 255, 0)  
red = (255, 0, 0)    

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "YQ2PNEN438H27L0G"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature,humidity,weather_condition,employeeId,employee,is_ontime, urlString):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature,
        'field2': humidity,
        'field3': weather_condition,
        'field4': employeeId,
        'field5': employee,
        'field6': is_ontime, 
        'field7': urlString,
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   

while True:
 
    for event in sense.stick.get_events():
        print(event.direction, event.action) 
        if event.action == "pressed":
         capture_image(IMAGE_PATH)
         print("Image captured using SenseHAT button")

         blynk.log_event("clockin")

         deviceId= "anydevice"
         data = get_employee_data(deviceId)
         temperature = data['temp']
         humidity = data['humidity']
         #employeeId = data['employeeId']
         employee = data['employee']
         is_ontime = data['time_keeping']
         weather_condition = data['weather_condition']
         urlString=data['URL']

         employeeId = int(udp_data[0]["message"]) # not sure about this - I think I need a second thingspeak file
  
         print(f"Temperature: {temperature} C")
         print(f"Humidity: {humidity} ")
         print(f"Time Keeping: {is_ontime} ")
         print(f"EmpId: {employeeId} ")
         print(f"Emp: {employee} ")
         print(f"WeatherCondition: {weather_condition} ")
         print(f"URL: {urlString} ")
         

         if is_ontime:
                message=f"{employee} Ontime"
                sense.show_message(message, text_colour=green)               
         else:
                message=f"{employee} Late"   
                sense.show_message(message, text_colour=red)

        # Send the data to ThingSpeak
         send_to_thingspeak(temperature,humidity,weather_condition,employeeId,employee,is_ontime, urlString)   
        
        elif event.action == "released":
         print("Action complete")

      
    # Wait before the next reading 
    time.sleep(15)     
            
