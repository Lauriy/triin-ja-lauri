#!/bin/bash
export HOME=/home/triinjalauri
cd $HOME
source venv/bin/activate
cd $HOME/triinjalauri/
uwsgi --socket /home/triinjalauri/triinjalauri.sock --processes=1 --module triinjalauri.wsgi --chmod-socket=777 --env=LANG="en_US.utf8"
exit $?