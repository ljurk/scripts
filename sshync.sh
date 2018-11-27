#!/bin/sh
SRC=ljurk@horus:/media/hdd/nc_data/ljurk/files/pwd/ljurk.kdbx
DEST=/home/ljurk/
rsync -avz -e "ssh" $SRC $DEST
