# Installation écran OLED type SH1106

## Environnement virtuel Python
### Création
```
python3 -m venv ~/luma_env
```
### Installation
```
~/luma_env/bin/python -m pip install --upgrade luma.oled
```
```
~/luma_env/bin/python -m pip install pyserial
```
```
~/luma_env/bin/python -m pip install RPi.GPIO
```
###
Dépendances
```
sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 -y
```
Droits
```
sudo usermod -a -G gpio,i2c pibox
```

### Installer GIT
```
sudo apt install git
```

### cloner le dépot PiBox
```
git clone https://github.com/clbrn/PiBox.git clbrn
```
### Copie scripts Python affichage de l'environnement virtuel
```
sudo cp ~/clbrn/oled/scripts_py/*.py ~/luma_env
```
Rendre les scripts exécutables
```
sudo chmod +x ~/luma_env/aff_oled.py
```
```
sudo chmod +x ~/luma_env/aff_ini.py
```

### lancement du script d'affichage toute les minutes
```
sudo crontab -e
```
Ajouter la ligne dans crontab
```
*/1 * * * *          /home/pibox/luma_env/aff_oled.py
```
### Copie scripts Python affichage demarrage dans le répertoire /etc/init.d
```
sudo cp ~/clbrn/oled/scripts_sh/aff_ini.sh /etc/init.d
```
### Automatiser le lancement au démarrage
```
cd /etc/init.d
```
```
sudo chmod +x aff_ini.sh
```
```
sudo update-rc.d aff_ini.sh defaults
```
```
sudo reboot
```



