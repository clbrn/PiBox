#!/home/pibox/luma-env/bin/python
#
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
from time import sleep
from time import strftime
from datetime import datetime
import time
import serial
import RPi.GPIO as GPIO

def10 = ImageFont.load_default(10)
def12 = ImageFont.load_default(12)
def28 = ImageFont.load_default(29)
dvs12 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans",10)
dvs28 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans",28)

def antenne():
    draw.line((3, 3, 3, 10), fill=255)
    draw.line((4, 4, 4, 4), fill=255)
    draw.line((5, 3, 5, 3), fill=255)
    draw.line((2, 4, 2, 4), fill=255)
    draw.line((1, 3, 1, 3), fill=255)
    draw.line((0, 2, 0, 2), fill=255)
    draw.line((3, 2, 3, 2), fill=255)
    draw.line((6, 2, 6, 2), fill=255)

def signal(niv):
    if niv > 0:
          draw.line((15,10,15,8), fill=255)
          draw.line((16,10,16,8), fill=255)
    if niv > 8:
          draw.line((18,10,18,6), fill=255)
          draw.line((19,10,19,6), fill=255)
    if niv > 17:
          draw.line((21,10,21,4), fill=255)
          draw.line((22,10,22,4), fill=255)
    if niv > 26:
          draw.line((24,10,24,2), fill=255)
          draw.line((25,10,25,2), fill=255)

def code_apn():
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
    rep = oper.decode()
    print(rep)
    return rep

def code_signal():
    cmde = bytes(b'AT+CSQ\r')
    ser.write(cmde)
    time.sleep(0.1)
    rep_CSQ = ser.read(size=64)
    long = len(rep_CSQ)
    rep = rep_CSQ.decode()
    pos = rep.find("+CSQ: ") + 6
    stf = rep_CSQ[pos:long]
    pos = stf.find(b"\r")
    rep = stf[0:pos]
    stniv = rep.decode()
    stniv = stniv.replace(',',".")
    niv = float(stniv)    
    print(niv)
    return niv

def get_time():
    now = datetime.now() 
    tt = now.strftime("%H:%M")
    print("time:", tt)
    return tt

ser = serial.Serial('/dev/ttyUSB3', baudrate = 115200, timeout = 1,rtscts=True, dsrdtr=True)
ser.close()
ser.open()
apn = code_apn()
sig = code_signal()

seri2c = i2c(port=1, address=0x3C)

device = sh1106(seri2c)
device.clear

with canvas(device) as draw:
    antenne()
    signal(sig)
    time = get_time()
    draw.text((40, 0), apn, font=dvs12, fill=255)
    draw.text((28, 13), time, font=dvs28, fill=255)
    draw.text((17,50), "GW : 192.168.0.1", font=dvs12, fill=255)

sleep(2)


device.persist = True
