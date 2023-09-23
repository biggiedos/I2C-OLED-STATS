from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from lib_oled96 import ssd1306
from PIL import ImageFont, ImageDraw
from smbus import SMBus

# Set up a headless browser (you can also use a regular browser by removing 'headless')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')  # Required for running as root on Linux
options.add_argument('--disable-dev-shm-usage')  # Required for running on Raspberry Pi

# Create a ChromeService instance with the path to ChromeDriver
chrome_driver_path = '/usr/lib/chromium-browser/chromedriver'  # Adjust if needed
chrome_service = ChromeService(chrome_driver_path)

# Pass the ChromeService instance to the ChromeDriver
browser = webdriver.Chrome(service=chrome_service, options=options)

# URL of the webpage you want to connect to
url = "http://192.168.1.5:8085"

# Initialize the OLED display
i2cbus = SMBus(1)  # Use 1 for Raspberry Pi 2 and newer, use 0 for Raspberry Pi 1
oled = ssd1306(i2cbus)
draw = oled.canvas

# Setup fonts
font_path = '/home/danmo/oled/FreeSans.ttf'
font1 = ImageFont.truetype(font_path, 36)
font2 = ImageFont.truetype(font_path, 20)
font3 = ImageFont.truetype(font_path, 12)

while True:
    try:
        # Load the webpage or refresh the current page
        browser.get(url)
        print("get url")
        # Wait for a few seconds to ensure JavaScript has a chance to execute (adjust as needed)
        browser.implicitly_wait(10)

        # Find the "CPU Core" row and the corresponding "Value" column
        cpu_core_row = browser.find_element(By.XPATH, '//tr[./td[contains(text(), "CPU Core")]]')
        value_column = cpu_core_row.find_element(By.XPATH, './td[contains(@data-bind, "text: Value")]')
        print("get value")
        # Get the value from the "Value" column
        cpu_core_value = value_column.text

        # Clear the OLED display
        draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=0, fill=0)
        print("clear oled")
        # Display the CPU Core value and "CPU Temp" on the OLED display using font3
        draw.text((0, 0), cpu_core_value, font=font1, fill=1)
        draw.text((0, 40), "CPU Temp", font=font2, fill=1)

        oled.display()
        print("write")
        # Sleep for 5 seconds before the next refresh
        time.sleep(1.5)

    except KeyboardInterrupt:
        break  # Exit the loop if Ctrl+C is pressed
    except Exception as e:
        # Display "No connection" in font3 on the OLED display if an exception is thrown
        draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=0, fill=0)
        draw.text((0, 0), "No connection", font=font3, fill=1)
        oled.display()
        print(f"An error occurred: {e}")

# Close the browser and OLED display when done
browser.quit()
oled.cls()
oled.display()
