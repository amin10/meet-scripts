#!/bin/bash
#Wait for Network to be available
while true
do
sudo ping -c 1 https://raw.githubusercontent.com/amin10/meet-scripts/master/onreboot.sh
if [[$?==0]];
then
echo 'Network available.'
break;
else
sleep 5
fi
done
sudo wget https://raw.githubusercontent.com/amin10/meet-scripts/master/onreboot.sh
sudo chmod +x onreboot.sh
sudo ./onreboot.sh
sudo rm onreboot.sh
