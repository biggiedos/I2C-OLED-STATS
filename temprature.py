from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from lib_oled96 import ssd1306
from PIL import ImageFont, ImageDraw
from smbus import SMBus

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'  # Change to actual path if you've changed the default install path
chrome_service = ChromeService(chrome_driver_path)

browser = webdriver.Chrome(service=chrome_service, options=options)

url = "http://your_ip:8085" #set url with ip and port of OWMr web server. 8085 is the default port but you may need to changethis if you change the default port 

i2cbus = SMBus(1)  # Use 1 for Raspberry Pi 2 and newer, use 0 for Raspberry Pi 1
oled = ssd1306(i2cbus)
draw = oled.canvas

font_path = '/home/danmo/oled/FreeSans.ttf' #select font. I've included one as default
font1 = ImageFont.truetype(font_path, 36)
font2 = ImageFont.truetype(font_path, 24)
font3 = ImageFont.truetype(font_path, 12)

while True:
    try:
        browser.get(url)
        browser.implicitly_wait(10)

        cpu_core_row = browser.find_element(By.XPATH, '//tr[./td[contains(text(), "CPU Core")]]') #this gets the cpu core value from OHW. You could get GPU temprature for example.
        value_column = cpu_core_row.find_element(By.XPATH, './td[contains(@data-bind, "text: Value")]')
        cpu_core_value = value_column.text

        draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=0, fill=0) #comment out this line and uncomment the below line to have a nice refresh effect
        #oled.cls()
        draw.text((0, 0), cpu_core_value, font=font1, fill=1)
        draw.text((33, 40), "CPU", font=font2, fill=1)

        oled.display()
        time.sleep(1.5) #change to adjust how quick the browser refreshes. It's untested for refreshing lower than every 1.5s

    except KeyboardInterrupt:
        break
    except Exception as e:
        draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=0, fill=0)
        #oled.cls()
        draw.text((0, 0), "TIMEOUT", font=font2, fill=1)
        oled.display()
        print(f"An error occurred: {e}")

browser.quit()
oled.cls()
oled.display()
