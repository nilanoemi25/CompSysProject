from employee_data import get_employee_data
from sense_hat import SenseHat

deviceId = "anything"
data = get_employee_data(deviceId)


# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
    #deviceID = "myDevice001"
    data = get_employee_data(deviceId)
    # Print the data in JSON format for testing
    print(data)