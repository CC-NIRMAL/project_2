from machine import Pin
import utime
import sys

# Define pins
PIR_PIN = 14
LED_PIN = 2

# Set up PIR sensor and LED
pir = Pin(PIR_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)

def log_motion(timestamp):
    try:
        # Send log data over serial
        print(f"Motion detected at: {timestamp}")  # Sends log to serial port
    except Exception as e:
        print(f"Failed to log motion: {e}")

def get_timestamp():
    # Get current time (dummy for MicroPython; replace with RTC or network time if available)
    t = utime.localtime()
    return "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(t[0], t[1], t[2], t[3], t[4], t[5])

print("Setup complete.")

while True:
    if pir.value() == 1:  # Motion detected
        print("Motion detected!")  # This will be sent to serial
        led.value(1)  # Turn on LED
        
        # Get timestamp and log
        timestamp = get_timestamp()
        log_motion(timestamp)
        
        utime.sleep(2)  # Debounce delay
        led.value(0)  # Turn off LED
