# Installation a partir de l'Image Disque
## Téléchargement Image
Télécharger l'image disque "PiBox_Orange.img.gz" dans la Release "Image Disque".
<img width="1279" height="437" alt="Capture d’écran 2026-06-15 à 08 34 31" src="https://github.com/user-attachments/assets/2801ed04-86c6-41c1-996f-44067ea1570d" />
Décompresser le fichier.   

## Ecriture carte SD
Graver le fichier PiBox_Orange.img sur la carte SD (option "utiliser une image personnalisée" de "Raspberry Pi Imager".   

   
## Changer le mot de pasee du Hotspot
Désactiver le Hotspot
```
sudo nmcli con down PiBox
```
Modifier le mot de passe
```
sudo nmcli con modify PiBox wifi-sec.psk votrenouveaupassword
```
Résactiver le Hotspot
```
sudo nmcli con up PiBox
```
