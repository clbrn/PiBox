# PiBox
Raspberry Routeur 4G / 5G 
# Installation
## Gravage PI OS (sur Mac)
Utilisation de **Raspberry Pi Imager**   
image :  **PI OS Bookworm 64 Bit lite**   
nom de l'hote : **PiBox**   
utilisateur  : _pibox_   
mot de passe : _pibox_   

## Mise a jour configuration Raspberry
Activation du port serie et parametrage du pay pour le WiFi   
```
sudo raspi-config
```
### Port Serie
Choix **3** _Interface Option_, puis choix **I6** _Serial Port_
répondre **Non** à la première question et **Oui** à la deuxième   
Puis encore **Oui** pour valider   
### Pays Wifi
choix **5** _Localisation Options_   
## cloner le dépot PiBox
```
git clone https://github.com/clbrn/PiBox.git
```

