#! /bin/sh

### BEGIN INIT INFO
# Provides:          aff_inio
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Affichage initial
# Description:       Lancement su script aff_ini.py au démarrage
### END INIT INFO

cd /home/pibox/luma_env
aff_ini.py
