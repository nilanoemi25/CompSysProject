![Static Badge](https://img.shields.io/badge/Noemi_Lovei-pink)
![Static Badge](https://img.shields.io/badge/Software_Student-SETU_2024-blue)
![Static Badge](https://img.shields.io/badge/Computer_Systems_Project-2024-red)
![Static Badge](https://img.shields.io/badge/HTTP-green)
![Static Badge](https://img.shields.io/badge/MQTT-purple)
![Static Badge](https://img.shields.io/badge/Python-green)



# Project Title
 HR Clocking System

# Project Description 
This project is 40% of CompSys module in semester two, year 1 Hdip in SETU. 

The purpose of this project is to explore different tools that a HR Assistant may use in office to track employee attendance/time-keeping. <br>

# Firstly: <br>
On Raspberry PI the physical trigger is to press **button** to simulate 'clock in punch'. <br>
1. When the button is pressed the temperature, humidity and time values are read, along with employeeID and employeeName.
2. A photo is taken of the employee as they clock in.  
3. The name of the employee & 'late' or 'ontime' message appears on the Raspberry PI SenseHat <br>
The temperature and humidity values are used to infer wether the weather is good or bad. <br>
Bad weather may be a valid excuse for lateness of an employee as it may cause commuting issues, traffic build up, accidents on the road etc <br>
Good weather there is no excuse of lateness of an employee <br>
The current time is measured against logic to determine whether the employee is late or ontime **at the button press.**<br>

## MQTT:
All of this information is linked with an MQTT protocol. The publishing is done via the client_pub.py script and the subscription can be via the client_sub.py script AND/OR via MQTT app on mobile. <br>
This allows the HR professional to get clock in punches and their information to their work mobile phones. <br>

Employee ID and employeeName are taken from the employee_data(base). <br>

### List of values:
+ "deviceID" 
+ "temp"
+ "humidity"
+ "employee"
+ "employeeId"
+ "weather_condition"
+ "time_keeping" 
+ "current_time"
+ "URL" 


## HTTP:
Data is sent to Thingspeak platform using HTTP protocol. <br>
The Thingspeak platform visualises the temperature and humidity which are integers on it's dashboard.<br>
An EmailHR React App is in place that will send an email to HR professional IF any employee is late. ( Only first lateness emailed in assignment to prevent too many emails.)<br>
Most importantly the data gathered from the Rasberry PI button press input, can be downloaded as an CSV file by HR professional where all fields (not just integers but strings also) can be used in office for deep diving.  <br>

### List of values:

+ 'field1': temperature,
+ 'field2': humidity,
+ 'field3': weather_condition,
+ 'field4': employeeId,
+ 'field5': employee,
+ 'field6': is_ontime, 
+ 'field7': urlString

***

The photo taken is stored on Glitch platform, full gallery accessible here: <br> https://glitch.com/~gentle-calico-nautilus <br>

![alt text](https://github.com/nilanoemi25/CompSysProject/blob/main/Miscellaneous/Img/glitch.PNG "Glitch") <br>


Of all the data gathered **humidity**, **temperature** and the **photo** are sent to Blynk platform. This makes it more user friendly for the HR professional to access the data in contrast to the MyMQTT app. 
A push notification is enabled for each employee clock in on the mobile phone. 

# Secondly: <br>

## Version 1 <br>
The Raspberry PI is linked to Packet Tracer with a network that has an RFID reader and an entrance door. <br>
I faced challenges retrieving data gathered via the RFID reader from the Iot Manager(Web Server) and so I placed the motion sensor next to the door/RFID reader and got information from the motion sensor instead. <br>
Next the motion sensor is activated. ( must be activted with ALT ).<br>
The idea is that when the employee walks in the door (IOT Manager fully set up in Packet Tracer), having successfully passed through the RFID validation the motion sensor actuates the Raspberry PI, which will light up in green AND print all relevant information (temp, humidity, employeeName, employeeId, **currentime stamp**, late/ontime) to the terminal, using the POST API. <br>

## Version 2 <br>
The Raspberry PI is linked to Packet Tracer and the RFID reader uses UDP to send the cardID to the PI.  <br>
The PI reads the temp, humidity and time stamp and sends this data along with RFID card ID to a JSON file.  <br>
A HTTP thingspeak script reads in this data from the json file and uses logic to determine 1) the name of the employee and 2) whether the employee was late or ontime.  <br>
Subsequently all this data is sent to ThingsSpeak platform, where it can be viewed and downloaded by the user.  <br>
The data is also sent to Blynk app with notifications enabled. 

# Additionally:  <br>
The restAPIs trigger different websites with templates, styled with some CSS, logically diving the data that was gathered from the Raspberry PI.<br>
***
/<br>
/sensehat/environment<br>
/sensehat/punctual<br>
/sensehat/punctualpost<br>
/sensehat/greenlight<br>

# How to Install / Run the project

You will need:
+ Raspberry PI
+ Sensehat
+ Camera for Raspberry PI
+ Desktop

## HTTP 

1. SSH from Desktop into Raspberry PI. 
2. Download from github and run thingspeak_data_http.py from Terminal using the python command.
3. Click the button on Raspberry PI to start the process.
4. View data collected in Thingspeak Web dashboard and Blynk Web dashboard /app. 

## MQTT

1. SSH from Desktop into Raspberry PI. 
2. Download from github and run client_pub.py from Terminal using python command.
3. Click the button on Raspberry PI to start the process.
4. Check MyMQTT app or run client_sub.py script to receive the subscriber messages. 

## PacketTracer Version 1

1. Download the "theproject.pkt" from this github.
2. Run the file.
3. Wait for the connection to set up among all devices in the network. Ensure that both door and RFID reader are red. 
4. (If door is not locked, go to Web Server, IOT Monitor and turn the door to locked). You may need to login using the IP address of the Webserver and admin/root user/password.
5. Go to Raspberry PI and run the script.
5. Bring the 1001 card over the RFID reader and watch as it and the door turn green.
6. Near the RFID reader is the motion sensor, hold ALT to activate the sensor. 
7. Notice the Raspberry PI turn green and real time data print in the terminal. 

## PacketTracer Version 2
1. Download theproject_v2.pkt
2. Run the file & make sure the RFID reader programme is running
3. Bring the cards over the RFID reader and you will see the cardId printed in the terminal
4. Download and run sensor_listener.py script on RasbPI. Now you will see the cardId from the RFID reader and additional data from PI be logged to a JSON script called udp_data.json
5. Download and run udp_thingspeak_data_http.py from the HTTP Thingspeak folder and run it from the PI's terminal. 
6. Observe the data sent to Thingspeak platform and Blynk app. 

For Step 4:
![alt text](https://github.com/nilanoemi25/CompSysProject/blob/main/Miscellaneous/Img/packetTracer.PNG "For step 4") <br>
For Step 5:
![alt text](https://github.com/nilanoemi25/CompSysProject/blob/main/Miscellaneous/Img/script.PNG "For step 5")

# Credits & Acknowledgements 
SETU 2024 classmates & teachers <br> 
Badges:<br> 
https://shields.io/badges <br> 
Github ReadMe Style:<br> 
https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet <br> 


# Licence
N/A

# Contact Information
Noemi Lovei 
20108892@mail.wit.ie 
