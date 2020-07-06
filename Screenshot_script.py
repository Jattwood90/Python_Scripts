from selenium import webdriver
import csv
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime

png = '.png'
mobi = '_mobi_'

def selenium_out():
    #opens Chrome, maximises screen and saves file in current directory of script
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    time.sleep(3)
    file = str(url[7:]+png)

    # browser.save_screenshot(file)
    browser.close()

def mobile_shot():
    mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

        "userAgent": "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36" }

    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options = options)
    driver.get(url)

    time.sleep(3)
    file = str(url[7:]+mobi+png)

    driver.save_screenshot(file)
    driver.close()

start_time = datetime.now()

with open('check.csv') as csvfile:
    #opens csv file, where list of URLs exist
    reader = csv.reader(csvfile)


    for i in csvfile:
        try:
            url = i.strip()
            #strip required to delete the '\n' that randomly appears at end of variable
            selenium_out()
            # mobile_shot()
        except:
            print(f"{url} could not be saved")
            continue

csvfile.close()

print("Script finished!")
time_taken = datetime.now() - start_time
print(f"This script took: {time_taken} to complete")


