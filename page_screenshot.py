from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

png = '.png'

def selenium_out():
    #opens Chrome, maximises screen and saves file in current directory of script
    browser = webdriver.Chrome(ChromeDriverManager().install()) #this overwrites the need to update chromedriver
    browser.get(url)
    browser.maximize_window()
    time.sleep(3)
    file = str(url[8:-1]+png)

    browser.save_screenshot(file)
    browser.close()


with open('path to csv file') as csvfile:
    #opens csv file, where list of URLs exist
    reader=csv.reader(csvfile)

    for i in csvfile:
        url = i.strip()
        #strip required to delete the '\n' that randomly appears at end of variable
        selenium_out()


csvfile.close()
print("Script finished!")


