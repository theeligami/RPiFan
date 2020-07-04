# RPiFan
A PWM fan speed controller for the raspberry pi.

## Getting started
These instructions will get you the latest version of the RPiFan fan control script installed. It will also add and activate a system service for to run the script automatically.

The repository also includes a [kicad](https://kicad-pcb.org/) project file so you can order the pcb from a manufacturer or design your own.
### Prerequisites
You need a working version of Raspberry Pi OS (formerly Raspbian) on your raspberry pi. You can get the latest version of Raspberry Pi OS [here](https://www.raspberrypi.org/downloads/).

Other debian-based distributions might work too, but are not officially supported by RPiFan.
### Connecting the pcb
![Connecting the RPiFan pcb](doc/images/connecting.svg?raw=true "How to connect the pcb to the raspberry pi GPIOs")

*[Original Image by Efa](https://commons.wikimedia.org/wiki/File:Raspberry_Pi_Zero_-_Location_of_connectors_and_ICs.svg) licensed under the [creative commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/legalcode)*

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

This project is licensed under the GPL 3.0 - see the [LICENSE.md](LICENSE.md) file for details
