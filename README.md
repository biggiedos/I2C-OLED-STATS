# I2C-OLED-STATS
view stats of a windows computer on an I2C oled that is connected to an SBC



## Getting started
The following project was made with and tested with Python 3.9.2  
The windiows machine is running Windows 11  
The I2C OLED is (128x64) is connected to a Raspberry pi 3a+ running Raspbian lite 32bit  
Selenium is used and needs to be installed  

## What you need to do on your windows machine
Download the **Release** directory and run the web server on port 8085 using the following command:  


## What you need to do on your SBC (Linux)
In the **temprature.py** file use a text editor to change the `chrome_driiver_path` to the path where chrome driver is located.

In the **temprature.py** file use a text editor and make the following additions for your use case  
change the `url` variable to the ip address and port you want to get teh data fromn. You may have to add an inbound firewall rule to allow access from your SBC.  

You may need to change the `SMBus` depending on what SBC you are using.
