import time
from azure.iot.device import IoTHubDeviceClient

# Connection string. 
CONNECTION_STRING = "HostName=iothub-jil0813.azure-devices.net;DeviceId=Device02;SharedAccessKey=4LzKttnUFjbUC5W7k+e+s4JFcx8cRS8p+pvu2Jvl/2U="

# Connects
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def listen_for_messages():
    print("Waiting for messages from IoT Hub...")

    while True:
        try:
            # Cloud-to-Device message
            received_message = client.receive_message()
            print(f"Received message from IoT Hub: {received_message.data.decode('utf-8')}")

            # Complete message, sends confirmation.
            client.complete_message(received_message)
            print("Message processed. Sending confirmation.")

        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(1)

try:
    listen_for_messages()
except KeyboardInterrupt:
    print("Program interrupted. Disconnecting...")
finally:
    # Disconnect
    client.disconnect()
