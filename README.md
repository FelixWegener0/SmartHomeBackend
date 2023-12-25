# SmartHomeBackend

# install

# add script to startup

in Terminal run:

- crontab -e

add this to the file:

- @reboot python /home/pi/project/SmartHomeBackend/main.py > /home/pi/project/SmartHomeBackend/output.log

this will run the Script on boot the > param will write all logs to a specific log file
