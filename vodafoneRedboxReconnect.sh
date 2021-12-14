# use "chmod +x ./seleniumModemResetter.py" before running on Linux  



if [ $(ls /usr/local/bin/ | grep "geckodriver" | wc -m) == 12 ]
then 
	#TODO logs when disconnected and tries to connect again

	PASSWORD=""
	declare -i i=0
	while true
	do
		sleep 1
		STATUS="$( ping -q -c 1 -W 1 google.com >/dev/null &&   echo true ||   echo false  )"
		if [ $STATUS == "false" ]
		then
			i+=1
		else
			i=0
		fi

		#TODO In case of disconnection for 4 seconds, try to reconnect
		if [ $i == 4 ]
		then
			echo "$(date) Tarihinde kesinti yaşandı." >> log
			python3 seleniumModemResetter.py $PASSWORD &> /dev/null
			i=0
			sleep 2

		fi
	done
else
	read  -p "Geckodriver bulunamadı. Otomatik olarak yüklenmesi için ENTER'a basın " 
	sudo apt-get -y install python3-pip
	pip3 install selenium  
	wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
	sudo sh -c 'tar -x geckodriver -zf ./geckodriver-v0.30.0-linux32.tar.gz -O > /usr/local/bin/geckodriver'
	sudo chmod +x /usr/local/bin/geckodriver
	rm geckodriver-v0.30.0-linux32.tar.gz*


fi


                                                                                                             
