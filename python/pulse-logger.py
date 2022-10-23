import serial
import binascii
import time

ser = serial.Serial('COM6', 115200, timeout=1, parity=serial.PARITY_NONE, rtscts=0)
prev_volume = 0
while 1:
    serial_rx = ser.read(1000)

    serial_rx_hex = binascii.hexlify(serial_rx).decode("utf-8")
    print(serial_rx_hex)

    if serial_rx_hex != '':
        pulses = int(serial_rx_hex, base=16)
    else:
        pulses = 0

    print('Pulses = ', pulses)

    f = open("pulse.txt", "a")
    f.write(serial_rx_hex + ' Pulses = ' + str(pulses) + '\n')


