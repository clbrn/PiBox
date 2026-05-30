# Installation via QMI
sudo apt update && sudo apt upgrade
sudo rpi-update
sudo raspi-config // serial port
dmesg | grep ttyUSB
lsusb -t
dmesg | grep qmi
sudo apt install minicom
