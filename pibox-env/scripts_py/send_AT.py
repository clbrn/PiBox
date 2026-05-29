###
# Porbleme conflit avec Network Manager. Pour que ce script fonctionne il faut libérer ttyUSB3
# Modifier le fichier /lib/udev/rules.d/77-mm-quectel-port-types.rules pour le modem EC25 et le port ttyUSB3
# en remplaçant 'ID_MM_PORT_TYPE_AT_SECONDARY' par 'ID_MM_PORT_IGNORE' 

import serial
import RPi.GPIO as GPIO
import time


print ("Quectel E25  -  Bonjour")
# Activation du port sére

print("Connecting Port..")

ser = serial.Serial('/dev/ttyUSB3', baudrate = 115200, timeout = 1,rtscts=True, dsrdtr=True)
ser.close()
ser.open()
cmde = bytes(b'AT+QSPN\r')
ser.write(cmde)
time.sleep(0.1)
rep_QSPN = ser.read(size=64)
#print(rep_QSPN)
long = len(rep_QSPN)
rep = rep_QSPN.decode()
pos = rep.find("+QSPN: ") + 8
stf = rep_QSPN[pos:long]
pos = stf.find(b",") - 1
oper = stf[0:pos]
print(oper.decode())
time.sleep(2)
cmde = bytes(b'AT+CSQ\r')
ser.write(cmde)
time.sleep(0.1)
rep_CSQ = ser.read(size=64)
#print(rep_CSQ)
long = len(rep_CSQ)
rep = rep_CSQ.decode()
pos = rep.find("+CSQ: ") + 6
stf = rep_CSQ[pos:long]
pos = stf.find(b"\r")
niv = stf[0:pos]
print(niv.decode())
ser.close
