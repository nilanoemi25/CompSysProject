from flask import Flask, request, render_template
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
if result.tm_min > 2 and result.tm_min < 45 and result.tm_min != 0:
        is_ontime = False 
    

sense.clear()  


@app.route('/sensehat/environment',methods=['GET'])
def current_environment():
    temperature=round(sense.temperature,2)
    humidity=round(sense.humidity,2)
    flag="default"
    if humidity > 90 and temperature < 20:
     flag = "It's probably raining today."
    else:
     flag = "The weather looks good today."

    msg = {"deviceID": deviceID,"temp":temperature,"humidity":humidity,"weather_conditions":flag}
    #return str(msg)+"\n"
    return render_template('environment.html', temperature=temperature, humidity=humidity, flag=flag)


@app.route('/sensehat/punctual',methods=['GET'])
def current_punctual():
 is_ontime = True
 seconds = time.time()
 result = time.localtime(seconds) 
 if result.tm_min > 2 < 30 or result.tm_min > 32 and result.tm_min != 0:
    is_ontime = False 
 if is_ontime:
    status = "Ontime"
 else:
    status = "Late"
    msg = {"deviceID": deviceID,"is_ontime":is_ontime,"punctual":status}
    #return str(msg)+"\n"
    return render_template('punctual.html', is_ontime=is_ontime, status=status)

#sensehat/punctualpost?is_ontime=True
@app.route('/sensehat/punctualpost',methods=['POST'])
def message_post():
    state=request.args.get('is_ontime')
    print (state)
    if (state=="True"):
        sense.show_message("Ontime", text_colour=green)
        return '{"state":"True"}'
    else: 
        sense.show_message("Late", text_colour=red)
        return '{"state":"False"}'


@app.route('/') 
def index():
    celcius = round(sense.temperature, 2)
    humidity = round(sense.humidity,2)
    return render_template('index.html', celcius=celcius, humidity=humidity)


app.run(host='0.0.0.0', port=5000, debug=True)


# Allow standalone testing of this module
#if __name__ == "__main__":
    # Example device ID and usage

"""
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
            
    
    time.sleep(16)  # Slight delay to avoid high CPU usage
    

""" 
