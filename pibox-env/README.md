# Installation écran OLED type SH1106

### Installer GIT
```
sudo apt install git
```

### cloner le dépot PiBox
```
git clone https://github.com/clbrn/PiBox.git
```
### Copie scripts Python affichage de l'environnement virtuel
```
sudo cp ~/pibox/pibox-env/scripts_py/aff_oled.py ~/luma-env
```
### Copie scripts Python affichage demarrage dans le répertoire /etc/init.d
```
sudo cp ~/pibox/pibox-env/scripts_py/aff_ini.py /etc/init.d
```
