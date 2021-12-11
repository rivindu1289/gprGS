import serial.tools.list_ports as port_list
import serial
ports = list(port_list.comports())
for p in ports:
    print (p)

with serial.Serial('COM3', 57600, timeout=5) as ser:
    # x = ser.read()          # read one byte
    # s = ser.read(10)        # read up to ten bytes (timeout)
    
    for i in range(10):
        line = ser.readline()
        print(line)