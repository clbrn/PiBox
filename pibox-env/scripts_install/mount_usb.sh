#! /bin/sh

### BEGIN INIT INFO
# Provides:       mount_nas
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: montage d'un repertoire NAS au demrrage
# Description:       montage  disque reseau
### END INIT INFO

sleep 10

sudo mount /dev/sda1 /mnt/usb
