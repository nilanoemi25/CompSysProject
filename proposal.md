# HR Clocking System

## Student Name : Noemi Lovei  StudentID : 20108892
This project is 40% of CompSys module in semester two, year 1 Hdip in SETU. 

The purpose of this project is to explore different tools that a HR Assistant may use in office to track employee attendance/time-keeping. <br>

Firstly: <br>
On Raspberry PI the physical trigger is to press **button** to simulate 'clock in punch'. <br>
When the button is pressed the temperature, humidity and time values are read, along with employeeID and employeeName.  <br>
The temperature and humidity values are used to infer wether the weather is good or bad. <br>
Bad weather may be a valid excuse for lateness of an employee. <br>
Good weather there is no excuse of lateness of an employee. <br>
The current time is measured against logic to determine whether the employee is late or ontime **at the button press.**<br>

All of this information is linked with an MQTT protocol. The publishing is done via the client_pub.py script and the subscription can be via the client_sub.py script AND/OR via MQTT app on mobile. <br>
This allows the HR professional to get clock in punches and their information to their work mobile phones. <br>

Employee ID and employeeName are taken from the employee_data(base). <br>

Secondly: <br>
The same information is sent to Thingspeak platform using HTTP protocol. <br>
The Thingspeak platform visualises the temperature and humidity which are integers.<br>
An EmailHR React App is in place that will send an email to HR professional IF any employee is late. ( Only first lateness emailed in assignment to prevent too many emails.)<br>
Most importantly the data gathered from the Rasberry PI button press input, can be downloaded as an CSV file by HR professional where all fields (not just integers but strings also) can be used in office for deep diving.  <br>

Thirdly: <br>
The Raspberry PI is linked to Packet Tracer with a network that has an RFID reader and an entrance door. <br>
Next to the RFID reader and the entrance there is also a motion sensor. ( must be activted with ALT ).<br>
The idea is that when the employee walks in the door (IOT Manager fully set up in Packet Tracer), having successfully passed through the RFID validation the motion sensor actuates the Raspberry PI, which will light up in green AND print all relevant information (temp, humidity, employeeName, employeeId, **currentime stamp**, late/ontime) to the terminal, using the POST API. <br>

The restAPIs trigger different websites, styled with some CSS, logically diving the data that was gathered from the Raspberry PI.<br>
/<br>
/sensehat/environment<br>
/sensehat/punctual<br>
/sensehat/punctualpost<br>
/sensehat/greenlight<br>



## Tools, Technologies and Equipment
+Rasberry Pi 5<br>
+Sensehat<br>
+Packet Tracer<br>
+Python <br>
+HTML <br>
+MQTT and MQTT app <br>
+HTTP<br>
+Thingspeak <br>
+Blynk - to do - probably not due to installation issues with Python 

## Project Repository
https://github.com/nilanoemi25/CompSysProject/tree/main 

