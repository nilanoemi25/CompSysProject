import socket
import threading
import json
import time 
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
humidity = sense.get_humidity()

flag="default"
if humidity > 15 and temp < 35:
    flag = "It's probably raining today.Employees may be late due to adverse weather conditions."
else:
     flag = "The weather looks good today. Employees have no excuse to be late."


current_time = time.strftime("%H:%M:%S", time.gmtime())

class SensorListener:
    def __init__(self, host='0.0.0.0', port=5000, buffer_size=1024):
        #Initialise the UDP Listener.
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.running = False
        self.callback = None

    def start(self):      
        #Start in a separate thread.
        self.running = True
        threading.Thread(target=self._listen, daemon=True).start()

    def stop(self):
        #Stop the UDP listener.
        self.running = False

    def _listen(self):
        #Internal method to listen for UDP packets and handle them.
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.bind((self.host, self.port))
            print(f"UDP Listener started on {self.host}:{self.port}")

            data_list =[]

            while self.running:
                try:
                    data, address = server.recvfrom(self.buffer_size)
                    message = data.decode()
                    print(f"Received data: {data.decode()} from {address}")

                     #Append received message to the list 
                    data_list.append({"message": message, "address": address, "time_stamp":current_time, "temperature":temp, "humidity":humidity, "flag":flag})
                     # Write the data list to a JSON file 
                    with open("udp_data.json", "w") as json_file: json.dump(data_list, json_file, indent=4)
    
                    if self.callback:
                        self.callback(data.decode())
                except Exception as e:
                    print(f"Error receiving data: {e}")
            print("UDP Listener stopped.")


if __name__ == "__main__":
    # Example usage
    def handle_data(data):
        print(f"Card Id: {data}")

    listener = SensorListener(port=5000)
    listener.callback=handle_data
    listener.start()

    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        listener.stop()