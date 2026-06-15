# Installation a partir de l'Image Disque
## Téléchargement Image
Télécharger l'image disque "PiBox_Orange.img.gz" dans la Release "Image Disque".
<img width="1279" height="437" alt="Capture d’écran 2026-06-15 à 08 34 31" src="https://github.com/user-attachments/assets/2801ed04-86c6-41c1-996f-44067ea1570d" />

<img width="1287" height="524" alt="Capture d’écran 2026-06-15 à 08 59 37" src="https://github.com/user-attachments/assets/33527cc8-8b9b-489d-bd38-368cecfe1385" />

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

<img width="924" height="112" alt="image" src="https://github.com/user-attachments/assets/02cb32ca-90cd-4ceb-a47f-c7ef1c89b31c" />

