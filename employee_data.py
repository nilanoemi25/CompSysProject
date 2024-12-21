from sense_hat import SenseHat
import time
from datetime import datetime
from upload_image import upload_image
import json
import BlynkLib

#Lets say that Sherlock starts at 9 am, James at 10 am, John at 11am and Irene at 12 noon etc 

emp_db = ''' { 
       "employees": [
          {
          "name": "Sherlock Holmes",
          "emp_id": 1111,
          "start_time": 9
          },
          {
            "name": "James Moriarty",
            "emp_id": 1112,
            "start_time": 10
          },
          {
            "name": "John H Watson",
            "emp_id": 1113,
            "start_time": 11
          },
          {
            "name": "Irene Adler",
            "emp_id": 1114,
            "start_time": 12
          },
          {
            "name": "Mary Morstan",
            "emp_id": 1115,
            "start_time": 13
          },
          {
            "name": "Mycroft Holmes",
            "emp_id": 1116,
            "start_time": 14
          },
          {
            "name": "Detective Lestrade",
            "emp_id": 1117,
            "start_time": 15
          },
          {
            "name": "Mrs Hudson",
            "emp_id": 1118,
            "start_time": 16
          },
          {
            "name": "Molly Hooper",
            "emp_id": 1119,
            "start_time": 17
          },
          {
            "name": "Guest",
            "emp_id": 9999,
            "start_time": "NULL"
          }
        ]
    } '''
              




# Blynk authentication token
BLYNK_AUTH = 'z275UI1-xYpfjeR4JM-TroJ1R4l28_HN'
IMAGE_PATH="../images/sensehat_image.jpg"
# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Initialize SenseHAT
sense = SenseHat()

# Register handler for virtual pin V1 write event
@blynk.on("V0")
def handle_v0_write(value):
    button_value = value[0]
    print(f'Current button value: {button_value}')
    if button_value=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()
    blynk.virtual_write(1, sense.temperature) 
    blynk.virtual_write(2, sense.humidity) 
    blynk.virtual_write(3, sense.pressure) 
   

def get_employee_data(deviceID):
  
    db = json.loads(emp_db)
    # I wont know which employee is clocking in. 
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    flag="default"
    if humidity > 15 and temp < 35:
     flag = "It's probably raining today.Employees may be late due to adverse weather conditions."
    else:
     flag = "The weather looks good today. Employees have no excuse to be late."

    current_time = datetime.now()
    current_time_pretty = f"Photo taken at {current_time:%H:%M}"
    url = str(upload_image(IMAGE_PATH))
    urlString = url.replace("http://", "hxxp://") #Changing URL to allow it to upload to Thingspeak, CSV file, field 7

    blynk.set_property(4,"urls", url)

#Logic for button press on Rasb Pi timekeeping:

    is_ontime = True
    seconds = time.time()
    result = time.localtime(seconds) 
    if result.tm_hour >= 9 and result.tm_hour < 10:
         employee = db['employees'][0]['name']
         employeeId = db['employees'][0]['emp_id']
    elif result.tm_hour >= 10 and result.tm_hour < 11:
        employee = db['employees'][1]['name']
        employeeId = db['employees'][1]['emp_id']
    elif result.tm_hour >= 11 and result.tm_hour < 12:
        employee = db['employees'][2]['name']
        employeeId = db['employees'][2]['emp_id']
    elif result.tm_hour >= 12 and result.tm_hour < 13:
        employee = db['employees'][3]['name']
        employeeId = db['employees'][3]['emp_id']
    elif result.tm_hour >= 13 and result.tm_hour < 14:
        employee = db['employees'][4]['name']
        employeeId = db['employees'][4]['emp_id']    
    elif result.tm_hour >= 14 and result.tm_hour < 15:
        employee = db['employees'][5]['name']
        employeeId = db['employees'][5]['emp_id']    
    elif result.tm_hour >= 15 and result.tm_hour < 16: 
        employee = db['employees'][6]['name']
        employeeId = db['employees'][6]['emp_id']      
    elif result.tm_hour >= 17 and result.tm_hour < 18:
        employee = db['employees'][7]['name']
        employeeId = db['employees'][7]['emp_id']     
    elif result.tm_hour >= 18 and result.tm_hour < 19:   
        employee = db['employees'][8]['name']
        employeeId = db['employees'][8]['emp_id']                     
    else:
        employee="Guest"
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
        "URL": urlString,
        
    }
    
    return data



if __name__ == "__main__":
    get_employee_data("anydeviceId")
    data = get_employee_data("anydeviceId")
    print(data)