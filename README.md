# SmartHomeBackend

# install

# add script to startup

in Terminal run:

- crontab -e

add this to the file:

- @reboot python /home/pi/project/SmartHomeBackend/main.py > /home/pi/project/SmartHomeBackend/output.log

this will run the Script on boot the > param will write all logs to a specific log file

# install FSTP use port 22

- sudo apt install vsftpd
- sudo nano /etc/vsftpd.conf
- replace content with:

anonymous_enable=NO

local_enable=YES

write_enable=YES

local_umask=022

chroot_local_user=YES

user_sub_token=$USER

local_root=/home/$USER/FTP

- mkdir -p /home/pi/FTP/files
- chmod a-w /home/pi/FTP
- sudo service vsftpd restart

### use command to copy files to the used folder

- sudo cp -a /home/pi/FTP/files/. /destination
