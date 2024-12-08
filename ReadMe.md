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
+"deviceID"
+"temp"
+"humidity"
+"employee"
+"employeeId"
+"weather_condition"
+"time_keeping" 
+"current_time"
+"URL" 


## HTTP:
Data is sent to Thingspeak platform using HTTP protocol. <br>
The Thingspeak platform visualises the temperature and humidity which are integers on it's dashboard.<br>
An EmailHR React App is in place that will send an email to HR professional IF any employee is late. ( Only first lateness emailed in assignment to prevent too many emails.)<br>
Most importantly the data gathered from the Rasberry PI button press input, can be downloaded as an CSV file by HR professional where all fields (not just integers but strings also) can be used in office for deep diving.  <br>

### List of values:

+'field1': temperature,
+'field2': humidity,
+'field3': weather_condition,
+'field4': employeeId,
+'field5': employee,
+'field6': is_ontime, 
+'field7': urlString

***

The photo taken is stored on Glitch platform, full gallery accessible here: [https://glitch.com/~gentle-calico-nautilus]

Of all the data gathered **humidity**, **temperature** and the **photo** are sent to Blynk platform. This makes it more user friendly for the HR professional to access the data in contrast to the MyMQTT app. 
A push notification is enabled for each employee clock in on the mobile phone. 

# Secondly: <br>
The Raspberry PI is linked to Packet Tracer with a network that has an RFID reader and an entrance door. <br>
I faced challenges retrieving data gathered via the RFID reader from the Iot Manager(Web Server) and so I placed the motion sensor next to the door/RFID reader and got information from the motion sensor instead. <br>
Next the motion sensor is activated. ( must be activted with ALT ).<br>
The idea is that when the employee walks in the door (IOT Manager fully set up in Packet Tracer), having successfully passed through the RFID validation the motion sensor actuates the Raspberry PI, which will light up in green AND print all relevant information (temp, humidity, employeeName, employeeId, **currentime stamp**, late/ontime) to the terminal, using the POST API. <br>

The restAPIs trigger different websites with templates, styled with some CSS, logically diving the data that was gathered from the Raspberry PI.<br>
***
/<br>
/sensehat/environment<br>
/sensehat/punctual<br>
/sensehat/punctualpost<br>
/sensehat/greenlight<br>


