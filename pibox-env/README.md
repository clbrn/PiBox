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
sudo cp ~/PiBox/pibox-env/scripts_py/*.py ~/luma-env
```
Rendre les scripts exécutables
```
sudo chmod +x ~/luma-env/aff_oled.py
```
```
sudo chmod +x ~/luma-env/aff_ini.py
```

### lancement du script d'affichage toute les minutes
```
sudo crontab -e
```
Ajouter la ligne dans crontab
```
*/1 * * * *          /home/pibox/luma-env/aff_oled.py
```
### Copie scripts Python affichage demarrage dans le répertoire /etc/init.d
```
sudo cp ~/PiBox/pibox-env/scripts_py/aff_ini.py /etc/init.d
```
### Automatiser le lancement au démarrage
```
cd /etc/init.d
```
```
sudo update-rc.d aff_ini.py defaults
```
```
sudo reboot
```


