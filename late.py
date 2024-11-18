from sense_hat import SenseHat
import time

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

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action) #print released
        if event.action == "pressed":

           # seconds = time.time()
           # result = time.localtime(seconds) 
           # print("result:", result) #
            print("\nhour:", result.tm_hour)
            print("minute:", result.tm_min)
            
            if is_ontime:
                sense.show_message("Ontime", text_colour=green)
            else:
                sense.show_message("Late", text_colour=red)
            is_ontime = not is_ontime

    time.sleep(0.3)  # Slight delay to avoid high CPU usage