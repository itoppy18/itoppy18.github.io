#!/bin/sh
#©2018 Mamoru Itoi

hour=04
minute=00

while :
do
	nowHour=`date "+%H"`
	nowMinute=`date "+%M"`
	if [ $nowHour = $hour ]; then
		if [ $nowMinute = $minute ]; then
			echo "起きてください"
			sudo chmod a+w /sys/class/gpio/export
			sudo echo 3 > /sys/class/gpio/export
			sudo chmod a+w /sys/class/gpio/gpio3/direction
			sudo echo out > /sys/class/gpio/gpio3/direction
			sudo chmod a+w /sys/class/gpio/gpio3/value
			sudo echo 1 > /sys/class/gpio/gpio3/value
			break
		fi
	fi
done
