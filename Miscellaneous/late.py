from sense_hat import SenseHat
import time

deviceID="device1"
sense = SenseHat()

# Define colours
green = (0, 255, 0)  
red = (255, 0, 0)    

# Initial state
is_ontime = True
seconds = time.time()
result = time.localtime(seconds) 
if result.tm_min > 2 < 30 or result.tm_min > 32 and result.tm_min != 0:
    is_ontime = False 

sense.clear()  

# GET data from Pi
def get_environmental_data():
# Retrieve temperature and humidity
 temp = sense.get_temperature()
 humidity = sense.get_humidity()

 """
  if humidity > 90 and temp < 20:
    return '{"It's probably raining"}' 
 else:
  return '{"It looks like good weather"}'
 """

 # Create a dictionary
 """data = {
    "deviceID": deviceID,
    "temp": round(temp, 2),
    "humidity": round(humidity, 2)
    } """
 
 return temp, humidity
 
def check_rain_conditions(temp, humidity):
 if humidity > 90 and temp < 20:
    print("It's probably raining.") 
 else:
  print("It looks like good weather.")


# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
     check_rain_conditions(15,74)

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action) #print released
        if event.action == "pressed":

            print("\nhour:", result.tm_hour) #Instead of printing I want to GET it and then POST it
            print("minute:", result.tm_min)
            
            if is_ontime:
                sense.show_message("Ontime", text_colour=green)
            else:
                sense.show_message("Late", text_colour=red)
            #is_ontime = not is_ontime

    time.sleep(0.3)  # Slight delay to avoid high CPU usage

