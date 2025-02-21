import serial
import time

# Set up serial connection (adjust port and baudrate as needed)
ser = serial.Serial('COM3', 115200)  # Replace 'COM3' with your actual serial port (e.g., '/dev/ttyUSB0' on Linux)
time.sleep(2)  # Allow some time for the connection to establish

def write_to_log(data):
    try:
        log_path = r"C:\Users\bacha\Desktop\micro\log.txt"
        with open(log_path, "a") as log_file:
            log_file.write(data)
        print(f"Logged: {data}")
    except Exception as e:
        print(f"Error writing to log file: {e}")

print("Listening for motion logs...")

while True:
    if ser.in_waiting > 0:  # Check if there's data from the microcontroller
        log_data = ser.readline().decode('utf-8').strip()  # Read the data and decode it
        if log_data:
            write_to_log(log_data + '\n')
