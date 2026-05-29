# PiBox
Raspberry Routeur 4G / 5G 
# Installation
## Gravage PI OS (sur Mac)
Utilisation de **Raspberry Pi Imager**   
image :  **PI OS Bookworm 64 Bit lite**   
nom de l'hote : **PiBox**   
utilisateur  : _pibox_   
mot de passe : _pibox_   

## connexion au Raspberry avec le Mac
Le Raspbery est connecté au réseau local via Ethernet, recherche de l'adresse ip : pour moi 192.168.1.34 (j'utilise Angry IP Scaner) 
connexion au Mac avec le terminal
```
ssh pibox@192.168.1.34
```
<img width="791" height="282" alt="image" src="https://github.com/user-attachments/assets/51e6fce4-5148-412f-9fae-56f6403598ef" />


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

## Mise à niveau PI OS
```
sudo apt update && sudo apt upgrade   
```

## installation des paquets nécessaires pour le modem
```
sudo apt install libqmi-utils udhcpc minicom modemmanager
```
puis faire un Reboot   

## Vérification Modem
<img width="719" height="142" alt="image" src="https://github.com/user-attachments/assets/a0f0f035-68aa-4fe6-a9aa-4882d9aa86c1" />

## Vérifier la connexion du modem avec minicom
```
sudo minicom -b 115200 -D /dev/ttyUSB2
```
Passer les commande ATE puis AT
Réponses attendues Ok (le premier ATE ne sera peut-etre pas visible si l'écho nest pas activé par défaut   
<img width="509" height="219" alt="image" src="https://github.com/user-attachments/assets/626f68c5-73a1-4d3a-88d7-3e25e438fe8e" />
   
Quitter minicom (_ctrl A puis X_)

## Identification Modem avec Modem Manager
```
sudo mmcli -L
```
<img width="763" height="111" alt="image" src="https://github.com/user-attachments/assets/559bd640-921f-4d3e-a332-e6792ee789ef" />

Ici modem 0   

## Activation du modem
```
sudo mmcli -m 0 --enable
```
<img width="632" height="117" alt="image" src="https://github.com/user-attachments/assets/64681260-4577-449d-9ec1-7698111a2e86" />

```
sudo mmcli -m 0 --simple-connect='apn=orange,ip-type=ipv4v6'
```   
<img width="674" height="101" alt="image" src="https://github.com/user-attachments/assets/1e0a7899-8c29-476f-8f26-96b1da4bd433" />

Recherche du Bearer
```
sudo mmcli -m 0
```
<img width="581" height="97" alt="image" src="https://github.com/user-attachments/assets/62079238-8a06-4cce-aef9-5680087ca95e" />

Le Bearer est tout à la fin, ici **1**  

```
sudo mmcli -m 0 -b 1
```
<img width="621" height="547" alt="image" src="https://github.com/user-attachments/assets/f75a89be-3c87-46ec-8c5c-a032d581236f" />
   
Modem connecté, adresse IP obtenue

## Activation wwan0
```
sudo ip link set wwan0 up
```

## Création de la connexion avec Network-Manager 
```
sudo nmcli connection add type gsm ifname '*' con-name 'orange' apn 'orange' connection.autoconnect yes
```
<img width="880" height="96" alt="image" src="https://github.com/user-attachments/assets/eedaaff8-c1e7-4a20-9a14-93b93206f0ae" />

Vérification des connexion et des Device Network Manager
<img width="764" height="210" alt="image" src="https://github.com/user-attachments/assets/f42069d5-c5d0-44cd-a897-75e18e5d1bd1" />


## cloner le dépot PiBox
```
git clone https://github.com/clbrn/PiBox.git
```

