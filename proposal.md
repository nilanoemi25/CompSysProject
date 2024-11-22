# HR Clocking System

## Student Name : Noemi Lovei  StudentID : 20108892
This project is 40% of CompSys module in semester two, year 1 Hdip in SETU. 

The purpose of this project is to explore different triggers that a HR Assistant may use in office to track employee attendance/time-keeping. 

In absence of RFID reader the **button** of Rasb PI will be used to trigger action and, the sensehat will show message on the screen such as "late" or "ontime" that would appear for the employee pressing the button.  

Thereafter information is sent to ThingsPeak using HTTP, where the HR professional can view and download and excel of the information gathered. In addition to timestamp, weather conditions are also forwarded so that deductions can be made from the data as to bad weather conditions causing excusable lateness by employees. An email will be sent to HR to alert them if employees are late. (Only first lateness to avoid overload)

Additionally MQTT will be used to send the same data to the HR Assistants mobile phone MQTT app. 

RFID is simulated as an IOT device in Packet Tracer and as the employee walks in the door, there is a motion sensor which actuates the PI to turn green. The script returns the actual timestamp to the terminal when the motion sensor is activated.  

## Tools, Technologies and Equipment
Rasberry Pi 5
Sensehat
Packet Tracer
Python 
HTML 
MQTT and MQTT app 
HTTP
Thingspeak 
Blynk - to do 

## Project Repository
https://github.com/nilanoemi25/CompSysProject/tree/main 

