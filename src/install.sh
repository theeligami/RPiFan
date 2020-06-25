#!/bin/bash
echo "Installing RPiFan - by Elias Kleimeier - https://github.com/theeligami"
mkdir /usr/local/sbin/RPiFan/
cp RPiFan.py /usr/local/sbin/RPiFan
echo "Done"

echo "Installing dependencies"
apt -y install python3
pip3 install -y RPi.gpio
echo "Done"

echo "Adding RPiFan to systemd service"
cp RPiFan.service /etc/systemd/system/RPiFan.service
echo "Done"

echo "Starting RPiFan.service"
systemctl enable RPiFan.service
echo "Done"

read -p "Would you like to reboot now? [y/N]: " input
if [ $input == "y" || $input == "Y" ]; then
	echo "Rebooting now"
	reboot
else
	echo "Changes will take effect after a reboot."
	echo "Bye!"
fi