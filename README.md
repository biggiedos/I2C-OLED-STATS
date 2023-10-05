# I2C-OLED-STATS
view stats of a windows computer on an I2C oled that is connected to an SBC



## Getting started
The following project was made with and tested with Python 3.9.2  
The windiows machine is running Windows 11  
The I2C OLED is (128x64) is connected to a Raspberry pi 3a+ running Raspbian lite 32bit  
Selenium is used and needs to be installed  

Before we start anything make sure all packages are up to date:  
`sudo apt update && sudo apt upgrade`  
## From a fresh install in user's home folder run:  
`sudo raspi-config`  
and under interface options, enable I2C.
now run:  
`sudo apt install i2c-tools`  
and verify the I2C oled is decteded by running:  
`i2cdetect -y 1`  
if you used the default I2C bus on the raspberry pi it shuld return the address 3c (0x3c) somewhere  
Install git if you havent already and clone the repository  
`git clone https://github.com/biggiedos/I2C-OLED-STATS`  
In the I2C-OLED-STATS directory you can ignore the release directory as that's meant to be run on a windows machine  
We will be installing Selenium using pip  
`pip install selenium`  
We will also install the ChromeDriver (This will take a while to install)  
`sudo apt install chromium-chromedriver`  
now you need to install the smbus library using pip:  
`pip install smbus-cffi`  
You also need to add the chromedriver path to to your .bashrc file using:  
`sudo nano ~/.bashrc`  
At the end of the file add:  
`export PATH=$PATH:/usr/lib/chromium-browser/`  
The program should now work! and you can run it by executing:  
`python temprature.py`  
After for the program to work properly you will now need to head over to your Windows machine and follow the instructions.
## What you need to do on your windows machine
Download the **Release** directory and run the web server on port 8085 using the following command:  


## Known issues
Sometimes when the windows machine is put into sleep it will not correctly contunie running the web server. The fixes for this are to either reboot, rerun the command to launch the web server or restart the task in task scheduler.  

I'm also aware of of the python program very rarely freezing and it will just display the last temprature. I'm pretty sure this is Selenium just randomly crashing as the python code is very simple.


In the **temprature.py** file use a text editor and make the following additions for your use case  
change the `url` variable to the ip address and port you want to get teh data fromn. You will have to add an inbound firewall rule to allow access from your SBC.  


