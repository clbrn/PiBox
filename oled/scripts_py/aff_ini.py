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

rep = subprocess.run(["runlevel"], capture_output=True, text=True)
level = rep.stdout
level =  level[0:3]
print(level)
if level == "N 3":
   txt1 = "   Arret en cours "
   txt2 = "    Au revoir..."
else:
   txt1 = "Démarrage en cours"
   txt2 = "Veuillez parienter..."

with canvas(device) as draw:
    draw.text((33, 4), "PiBox", font=dvs20, fill=255)
    draw.text((15, 30), txt1, font=dvs10, fill=255)
    draw.text((24, 45), txt2, font=dvs10, fill=255)

sleep(5)
device.persist = True

if level == "N 3":
   device.persist = False
   device.clear
else:
   subprocess.run(["/home/pibox/luma_env/aff_oled.py"])
