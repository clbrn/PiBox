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
Activation du port serie et parametrage du pays pour le WiFi   
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
## Partie Modem
### installation des paquets 
```
sudo apt install libqmi-utils udhcpc minicom 
```
puis faire un Reboot   

### Vérification Modem
<img width="719" height="142" alt="image" src="https://github.com/user-attachments/assets/a0f0f035-68aa-4fe6-a9aa-4882d9aa86c1" />

### Vérifier la connexion du modem avec minicom
```
sudo minicom -b 115200 -D /dev/ttyUSB2
```
Passer les commandes ATE puis AT.  
Réponses attendues Ok (le premier ATE ne sera peut-etre pas visible si l'écho nest pas activé par défaut   
<img width="509" height="219" alt="image" src="https://github.com/user-attachments/assets/626f68c5-73a1-4d3a-88d7-3e25e438fe8e" />
   
Quitter minicom (_ctrl A puis X_)

### Identification Modem avec Modem Manager
```
sudo mmcli -L
```
<img width="763" height="111" alt="image" src="https://github.com/user-attachments/assets/559bd640-921f-4d3e-a332-e6792ee789ef" />

Ici modem 0   

### Activation du modem
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

### Activation wwan0
```
sudo ip link set wwan0 up
```

### Création de la connexion avec Network-Manager 
```
sudo nmcli connection add type gsm ifname '*' con-name 'orange' apn 'orange' connection.autoconnect yes
```
<img width="880" height="96" alt="image" src="https://github.com/user-attachments/assets/eedaaff8-c1e7-4a20-9a14-93b93206f0ae" />

Vérification des connexions et des devices Network Manager
<img width="764" height="210" alt="image" src="https://github.com/user-attachments/assets/f42069d5-c5d0-44cd-a897-75e18e5d1bd1" />


A ce stade le Raspberry et connecté à Internet, mais la connexion n'est pas partagée.   
Vérification en faisant un ping sur l'interface wwan0
```
ping -c 5 -I wwan0 google.fr
```
<img width="812" height="211" alt="image" src="https://github.com/user-attachments/assets/8942854b-04d3-49c3-bf44-916defb5d137" />
  
**Ca fonctionne!**


## Partie Routeur
### installation des paquets 
```
sudo apt install dnsmasq iptables iptables-persistent
```

### Activation du forwarding
```
sudo nano /etc/sysctl.d/98-rpi.conf
```
Ajouter la ligne **net.ipv4.ip_forward=1** à la fin du fichier  

### Creation du Bridge et rattachement de l'interface eth0
```
sudo nmcli connection add type bridge con-name 'Bridge' ifname br0
```

```
sudo nmcli connection add type ethernet slave-type bridge con-name 'Ethernet' ifname eth0 master br0
```
<img width="863" height="114" alt="image" src="https://github.com/user-attachments/assets/61399ffd-8fd7-48da-9700-72ba16f887b7" />

### Céation du Hotspot rattaché au Bridge
```
sudo nmcli connection add con-name PiBox ifname wlan0 type wifi slave-type bridge master br0 wifi.mode ap wifi.ssid PiBox wifi-sec.key-mgmt wpa-psk wifi-sec.proto rsn wifi-sec.pairwise ccmp wifi-sec.psk votrepassword
```
<img width="984" height="102" alt="image" src="https://github.com/user-attachments/assets/64fe0515-74ce-48c0-9ba9-b9157c2382ce" />

### Mettre le Bridge en IP statique
```
sudo nmcli con mod "Bridge" ipv4.method manual ipv4.addresses 192.168.0.1/24
```

### Configuration de dnsmasq
```
sudo nano /etc/dnsmasq.conf
```
Ajout des lignes à la fin du fichier :
```
#
# PiBox
interface=br0
dhcp-range=192.168.0.10,192.168.0.100,12h
server=8.8.8.8
```

Faire un Reboot   
Déconnecter le Raspberry du réseau local   
Déconnecter le Mac du réseau local   
Connecter le Mac sur le port Ethernet du raspberry   

Aprés le reboot vérifier l'adresse IP du MAC   
<img width="523" height="398" alt="image" src="https://github.com/user-attachments/assets/eb1da1d8-76f5-40ec-b79d-9096a8959a7a" />

Le Mac est bien connecté à une adresse IP définie das le range de dnsmasq.   
La passerelle (le Raspbere a bien l'IP statique définie pour le Bridge).    
Il est possible de se reconnecter au Raspberry via le terminal du Mac avec l'IP de la passerelle.   
```
ssh pibox@192.168.0.1
```

Le Raspberry est connecté a internet, mais la connexion n'est pas encore partagés avec les appareils connectés par Ethernet ou par Wifi

### Mise en place des iptables
```
sudo iptables -t nat -A POSTROUTING -o wwan0 -j MASQUERADE
```
```
sudo iptables -A FORWARD -i eth0 -j ACCEPT
```
```
sudo iptables -A FORWARD -o eth0 -j ACCEPT
```
```
sudo iptables -A FORWARD -i wlan0 -j ACCEPT
```
```
sudo iptables -A FORWARD -o wlan0 -j ACCEPT
```

### iptables-persistent
```
sudo sh -c "iptables-save > /etc/iptables/rules.v4"
```
   
Maintenat le Mac peut accéder a Internet.   
Ouverture d'une nouvelle fenêtre du terminal sur le Mac.   
et faire in ping.   
<img width="657" height="280" alt="image" src="https://github.com/user-attachments/assets/1eb4da62-fadc-4e53-8e98-c84973ba8fb6" />

 **C'est tout Bon...**   


## Partie écran OLED SH1106
### Activation interface I2C et vérification
```
sudo raspi-config
```
Choix **3** _Interface Option_, puis choix **I5** _I2C_   
Répondre **Oui** puis valider et quitter

```
dmesg | grep i2c
```
<img width="980" height="101" alt="image" src="https://github.com/user-attachments/assets/ac3cb926-f388-4923-a317-262dc8767116" />
L'interface I2C est bien activée.   
   
Ajouter pibox au groupe I2C
```
sudo usermod -a -G i2c pibox
```
Installer i2c-tools   
```
sudo apt-get install i2c-tools
```
Vérification de l'adresse de l'écran
```
i2cdetect -y 1
```
<img width="463" height="188" alt="image" src="https://github.com/user-attachments/assets/c59b1726-936e-41fb-99b8-88f5065dc206" />

L'adresse de l'écran est 0x3C   

### Environnement virtuel
Création   
```
python3 -m venv ~/luma-env
```
Installation package luma-oledc  
```
~/luma-env/bin/python -m pip install --upgrade luma.oled
```
Installation package pyserial
```
~/luma-env/bin/python -m pip install pyserial
```
Installation des dependances
```
sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7
```
Mise a jour des droits
```
sudo usermod -a -G gpio,i2c pibox
```

### Conflit Modem Manager pyserial
Mes scripts python qui lance des commande AT sur ttyUSB3 plante car ttyUSB3 est bloqué par Modem Manager.   
```
sudo apt install lsof
```
```
sudo lsof /dev/ttyUSB3
```
<img width="594" height="84" alt="image" src="https://github.com/user-attachments/assets/bdf57d71-0de6-4692-97c0-c5c5433cb514" />
   
le process 668 de Modem Manager utilise le port ttyUSB3

Apres de longues recherches et beaucoup d'éssais infructueux, j'ai trouvé un palliatif qui fonctionne.   
Mais pas certain que ce soit tres orthodoxe.   

Modification du fichier /lib/udev/rules.d/77-mm-quectel-port-types.rules et ahout de ENV{ID_MM_DEVICE_IGNORE}="1" à la fin de la règle USB3 pour le module EC25
```
sudo nano /lib/udev/rules.d/77-mm-quectel-port-types.rules
```
Apès modification
<img width="1205" height="160" alt="image" src="https://github.com/user-attachments/assets/51598c2f-7e8d-4e3c-bf87-46641cc6cd0b" />
Vérification
```
sudo lsof /dev/ttyUSB3
```
Maintenant, le port ttyUSB3 est libre de toute utilisation.   
<img width="466" height="62" alt="image" src="https://github.com/user-attachments/assets/b683233a-2edf-4e16-8870-eb1803fe4c42" />






