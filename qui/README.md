# Installation via QMI
sudo apt update && sudo apt upgrade   
sudo rpi-update   
sudo raspi-config // serial port   
dmesg | grep ttyUSB   
lsusb -t   
dmesg | grep qmi   
sudo apt install minicom   
sudo apt install libqmi-utils udhcpc   
sudo qmicli -p -d /dev/cdc-wdm0 --device-open-net='net-raw-ip|net-no-qos-header' --wds-start-network="apn='orange', ip-type=4" --client-no-release-cid   
sudo udhcpc -q -f -i wwan0   
