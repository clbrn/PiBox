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
### Pays Wifi
choix **5** _Localisation Options_, puis choix **L4** _WLan Country_   
Choissir **"Fr"** dans la liste et valider   
### Port Serie
Choix **3** _Interface Option_, puis choix **I6** _Serial Port_
répondre **Non** à la première question et **Oui** à la deuxième   
Puis encore **Oui** pour valider  
Quitter (_Finish_) et accepter le Reboot   

## Vérification Modem
<img width="719" height="142" alt="image" src="https://github.com/user-attachments/assets/a0f0f035-68aa-4fe6-a9aa-4882d9aa86c1" />   

## Mise à niveau PI OS
```
sudo apt update && sudo apt upgrade   
```

## installation des paquets nécessaires pour le modem
```
sudo apt install libqmi-utils udhcpc minicom modemmanager
```
puis faire un Reboot

## cloner le dépot PiBox
```
git clone https://github.com/clbrn/PiBox.git
```

