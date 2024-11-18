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



# Initial state of button 
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
def current_punctual():
 is_ontime = True
 seconds = time.time()
 result = time.localtime(seconds) 
 if result.tm_min > 2 < 30 or result.tm_min > 32 and result.tm_min != 0:
    is_ontime = False 
 if is_ontime:
    punctual = "Ontime"
 else:
    punctual = "Late"
    msg = {"deviceID": deviceID,"punctual":punctual}
    return str(msg)+"\n"



app.run(host='0.0.0.0', port=5000, debug=True)


# Allow standalone testing of this module
#if __name__ == "__main__":
    # Example device ID and usage




while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action) 
        if event.action == "pressed":
            print("\nhour:", result.tm_hour) 
            print("minute:", result.tm_min)      
            if is_ontime:
                sense.show_message("Ontime", text_colour=green)
                message="Ontime"
            else:
                sense.show_message("Late", text_colour=red)
                message="Late"   
            
    
    time.sleep(30)  # Slight delay to avoid high CPU usage
    


