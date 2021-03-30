#   **********************************
#!/bin/csh

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

export PYTHON_HOME=/data/home/ubotapp/env/rsync-venv/bin
export PROJ_HOME=$HOME/app/util/rsyncher
export PROJ_NAME=$PROJ_HOME/src/main.py

if [ ! -z "`ps -eaf | grep java | grep $PROJ_NAME`" ]; then
    echo "$PROJ_NAME already started."
    exit
fi

$PYTHON_HOME/python $PROJ_NAME /data/home/ubotapp/tmp/rsync_test $PROJ_HOME/log/rsyncher.log &
echo "$PROJ_NAME started"
