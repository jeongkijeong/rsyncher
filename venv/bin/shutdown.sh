#   **********************************
#!/bin/csh

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi


PROJ_NAME=/data/home/ubotapp/app/util/rsyncher/src/main.py
PROC_LIST=`ps -ef | grep $PROJ_NAME | grep -v grep | awk '{print $2 }'`

for PID in $PROC_LIST
do
       kill $PID
done

echo $PROJ_NAME $PID 'stop'
