#!/bin/bash

# Make sure user is root
if [ "$EUID" -ne 0 ]; then
		ehco "Please run as root"
		exit
fi

read -p "Would you like to uninstall RPiFan Control by Elias Kleimeier? [y/N]: " input
if [ $input == "y" || $input == "Y" ]; then
		echo "Uninstalling"
		echo "Deleting /usr/local/sbin/RPiFan"
		rm -rf /usr/local/sbin/RPiFan
		echo "Done"

		echo "Stopping RPiFan system service"
		systemctl stop RPiFan.service
		echo "Disabling system service"
		systemctl disable RPiFan.service
		echo "Removing system service"
		rm -f /etc/systemd/system/RPiFan.service
		echo "Done"
else
		exit
fi
