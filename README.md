# RPiFan
A PWM fan speed controller for the raspberry pi.

## Getting started
These instructions will get you the latest version of the RPiFan fan control script installed. It will also add and activate a system service for to run the script automatically.
### Prerequisites
You need a working version of Raspberry Pi OS (formerly Raspbian) on your system. You can get the latest version of Raspberry Pi OS [here](https://www.raspberrypi.org/downloads/).
### Installing
Clone the repository to your raspberry pi.
```
git clone https://github.com/theeligami/RPiFan.git
```
Go to the directory of the install script
```
cd ./RPiFan/src
```
Mark the install script as executable
```
chmod +x install.sh
```
Run the install script as root
```
sudo ./install.sh
```

### Uninstalling
Mark the uninstall script as executable
```
sudo chmod +x /usr/local/sbin/RPiFan/uninstall.sh
```
Run the uninstall script
```
sudo /usr/local/sbin/RPiFan/uninstall.sh
```

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE.md](LICENSE.md) file for details
