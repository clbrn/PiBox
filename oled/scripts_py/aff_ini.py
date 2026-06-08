#!/home/pibox/luma_env/bin/python
#
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont
from time import sleep
import serial
import RPi.GPIO as GPIO
import subprocess

dvs20 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans",20)
dvs10 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans",10)

seri2c = i2c(port=1, address=0x3C)
device = sh1106(seri2c)
device.clear

with canvas(device) as draw:
    draw.text((33, 4), "PiBox", font=dvs20, fill=255)
    draw.text((15, 30), "Démarrage en cours", font=dvs10, fill=255)
    draw.text((24, 45), "Veuillez parienter...", font=dvs10, fill=255)

sleep(5)
device.persist = True
subprocess.run(["home/pibox/luma_env/aff_oled.py"])
