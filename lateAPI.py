from flask import Flask, request
from flask_cors import CORS
from sense_hat import SenseHat
import time

deviceID="NoemisPi"
sense = SenseHat()
sense.clear()

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

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

@app.route('/sensehat/environment',methods=['GET'])
def current_environment():
    temperature=round(sense.temperature,2)
    humidity=round(sense.humidity,2)
    flag="default"
    if humidity > 90 and temperature < 20:
     flag = "It's probably raining."
    else:
     flag = "The weather looks good."

    msg = {"deviceID": deviceID,"temp":temperature,"humidity":humidity,"weather_conditions":flag}
    return str(msg)+"\n"


@app.route('/sensehat/punctual',methods=['GET'])
def punctuality_get():
    #for event in sense.stick.get_events():
       # if event.action == "pressed":
           seconds = time.time()
           #is_ontime = "default"
           result = time.localtime(seconds) 
           if result.tm_min > 2 < 30 or result.tm_min > 32 and result.tm_min != 0:
            is_ontime = False 
            punctual="Late"
           else:
            is_ontime = True
            punctual ="Ontime"
            msg = {"deviceID": deviceID,"punctuality":punctual}        
            return str(msg)+"\n"


app.run(host='0.0.0.0', port=5000, debug=True)



# Allow standalone testing of this module
#if __name__ == "__main__":
    # Example device ID and usage


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

