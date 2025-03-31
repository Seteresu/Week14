import random
import time
from azure.iot.device import IoTHubDeviceClient, Message
import json

# COnnection string. 
CONNECTION_STRING = "HostName=iothub-jil0813.azure-devices.net;DeviceId=Device02;SharedAccessKey=4LzKttnUFjbUC5W7k+e+s4JFcx8cRS8p+pvu2Jvl/2U="

# Function for rng data
def get_sensor_data():
    temperature = random.uniform(20.0, 30.0)  # Simulating temperature in Celsius
    humidity = random.uniform(30.0, 70.0)  # Simulating humidity percentage
    return temperature, humidity

# Connect to the IoT
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

try:
    client.connect()

    # Sends data every 5 secs. 
    while True:
        # sensor data
        temperature, humidity = get_sensor_data()

        # payload in JSON format
        payload = {
            "temperature": temperature,
            "humidity": humidity
        }

        # converts payload
        message = Message(json.dumps(payload))

        # Send the message 
        client.send_message(message)
        print(f"Sent message to IoT Hub: {message}")

        # Wait before sending 
        time.sleep(5)

except KeyboardInterrupt:
    print("Program interrupted. Disconnecting...")

finally:
    Disconnects
    client.disconnect()
