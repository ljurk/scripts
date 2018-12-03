#!/bin/sh
SRC=ljurk@banan:/media/hdd/nc_data/ljurk/files/pwd/ljurk.kdbx
DEST=/home/ljurk/pwd
rsync -avz -e "ssh" $SRC $DEST
