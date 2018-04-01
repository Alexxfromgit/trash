#!/bin/bash

out_file=`dirname $0`"/task4_1.out"
exec 1>$out_file


MB1=`dmidecode -s baseboard-manufacturer`
MB2=`dmidecode -s baseboard-product-name`

MB=$MB1$MB2

SSN=`dmidecode -s system-serial-number`

echo "--- HardWare --"
echo "CPU: `cat /proc/cpuinfo | egrep "model name" -m1 | cut -c14-`" 
echo "RAM: `cat /proc/meminfo | egrep MemTotal | awk '{print $2" " $3}'`" 
echo "Motherboard: $MB"
echo "System Serial Number: $SSN"

echo "--- System ---"
echo "OS Distribution: `lsb_release -d --short`"
echo "Kernel version: `uname -r`"
echo "Installation date: `ls -clt / | tail -n 1 | awk '{ print $6, $7, $8 }'`"
echo "Hostname: `hostname`"
echo "Uptime: `uptime -p | cut -c4-`"
echo "Processes running: `ps -e | wc -l`"
echo "Users logged in: `uptime | cut -d "," -f 3 | cut -d " " -f 3`"

echo "--- Network ---"
for iface in $(ip addr list| grep "UP" | awk '{print $2}'|cut -d ":" -f 1|cut -d "@" -f 1)
   do
	IP=`ip addr list $iface | grep "inet "|awk '{print $2}'`
	if [ -z "${IP// /}" ] ; then IP="-" ; fi
	echo "$iface: $IP"
done
