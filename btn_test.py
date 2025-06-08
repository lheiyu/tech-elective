import serial

SERIAL_PORT = "COM4"
BAUD_RATE = 115200

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

while True:
    ln = ser.readline()
    print(ln)