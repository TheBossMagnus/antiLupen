import serial
import time

def send_serial_string(string_data):
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
    
    if not ser.is_open:
        ser.open()
        


    
    # Convert string to bytes if needed
    data_bytes = string_data.encode('utf-8')
    ser.write(data_bytes)
    
    # Close the connection
    ser.close()
        

if __name__ == "__main__":
    test_string = "1.255.000.000\n"   
    send_serial_string(test_string)