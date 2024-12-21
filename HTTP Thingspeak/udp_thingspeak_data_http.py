from sense_hat import SenseHat
import sys 
sys.path.insert(0, '../')
import requests
import time
#import datetime 
from employee_data import get_employee_data
from camera_test import capture_image
import BlynkLib
import json 

# Pull all data from udp_data.json
with open('../udp_data.json', 'r') as file: udp_data = json.load(file)
employeeId = int(udp_data[0]["message"])
time_stamp = udp_data[0]["time_stamp"]
temperature = float(udp_data[0]["temperature"])
humidity = float(udp_data[0]["humidity"])
flag = udp_data[0]["flag"]

is_ontime = True
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
def send_to_thingspeak(temperature,humidity,flag,employeeId,employee,is_ontime, urlString):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature,
        'field2': humidity,
        'field3': flag,
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

#Case to get employee to match the employee ID scan from RFID
def get_employee(employeeId):
    match employeeId:
        case 1111:
            return "Sherlock Holmes"
        case 1112:
            return "James Moriarty"
        case 1113:
            return "John H Watson"
        case 1114:
            return "Irene Adler"
        case 1115:
            return "Mary Morstan"
        case 1116:
            return "Mycroft Holmes"
        case 1117:
            return "Detective Lestrade"
        case 1118:
            return "Mrs Hudson"
        case 1119:
            return "Molly Hooper"
        case 9999:
            return "Guest"
    
       
#Timekeeping Logic
#Everyone works 9am to 5pm
def get_timekeeping(time_stamp):

  # start_time = "09:00:00"
   grace_period = "09:05:00"
   if time_stamp > grace_period:
       is_ontime = False
   return is_ontime

capture_image(IMAGE_PATH)
print("Image captured using SenseHAT button")

blynk.log_event("clockin")

deviceId= "anydevice"
data = get_employee_data(deviceId) # url = str(upload_image(IMAGE_PATH))
                                         #urlString = url.replace("http://", "hxxp://")

#weather_condition = data['weather_condition']
urlString=data['URL']

employee = get_employee(employeeId)
is_ontime = get_timekeeping(time_stamp)
         

print(f"Temperature: {temperature} C")
print(f"Humidity: {humidity} ")
print(f"Time Keeping: {is_ontime} ")
print(f"EmpId: {employeeId} ")
print(f"Emp: {employee} ")
print(f"WeatherCondition: {flag} ")
print(f"URL: {urlString} ")
         
# Send the data to ThingSpeak
send_to_thingspeak(temperature,humidity,flag,employeeId,employee,is_ontime, urlString)   


     
            
