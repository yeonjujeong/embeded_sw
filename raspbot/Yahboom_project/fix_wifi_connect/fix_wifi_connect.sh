#!/bin/bash


sudo cp -rf /etc/network/interfaces /etc/network/interfaces.backup
sudo cp -rf ./interfaces /etc/network/


sudo cp -rf ./wpa_supplicant.conf /etc/wpa_supplicant/

echo "Please reboot the system!"
