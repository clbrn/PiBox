#!/bin/bash

### sauvegarde 
datelog=$(date '+%b %d %H:%M:%S')
DATE=$(date +"%Y%m%d-%H%M")
user=$(whoami)
BoxToClone=pibox
jour=$(date '+%d')
joursem=$(date '+%u')

FileName=SD-Backup_$BoxToClone\_$DATE.img
File=/mnt/usb/backup/$FileName
Filegz=/mnt/usb/backup/$FileName.gz

#  echo "$datelog $user    jour $jour semaine $joursem debut de sauvegarde $rep $File" >> /var/log/messages

  sudo dd if=/dev/mmcblk0 | gzip --fast > $Filegz

  FileStat=$(wc -c "$Filegz" | cut -f 1 -d ' ')

  if [ $? -eq 0 ]; then
           Objet="SD-Backup $BoxToClone"
           Message="Clonage OK "
  else
          if [ -e $Filegz ]; then
                  sudo rm $Filegz
          fi
          Objet="SD-Backup $BoxToClone : ECHEC $?"
          Message="Echec du Clonage : fichier inexistant."
  fi

datelog=$(date '+%b %d %H:%M:%S')
# echo "$datelog $user    $Objet  $Message" >> /var/log/messages
