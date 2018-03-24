#!/bin/bash
#
# hostapd-wpe installation on Kali Linux
#
cd /tmp
git clone https://github.com/OpenSecurityResearch/hostapd-wpe
wget http://w1.fi/releases/hostapd-2.2.tar.gz
tar -zxf hostapd-2.2.tar.gz
cd hostapd-2.2
patch -p1 < ../hostapd-wpe/hostapd-wpe.patch 
cd hostapd
sed -i 's/#CONFIG_LIBNL32=y/CONFIG_LIBNL32=y/g' .config
make
chmod 755 hostapd-wpe
mkdir -p /usr/share/hostapd-wpe/certs
cp hostapd-wpe /usr/bin/hostapd-wpe
cp hostapd-wpe.eap_user /usr/share/hostapd-wpe/hostapd-wpe.eap_user
cd /tmp/hostapd-wpe/
cp -rf certs /usr/share/hostapd-wpe
chmod 755 /usr/share/hostapd-wpe/certs/bootstrap
#/usr/share/hostapd-wpe/certs/bootstrap

# Mofiy configuration file
