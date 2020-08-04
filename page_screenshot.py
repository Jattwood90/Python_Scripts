from selenium import webdriver
import csv
import time

def selenium_out():
    #opens Chrome, maximises screen and saves file in current directory of script
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    time.sleep(3)
    file = str(url[8:]+'.png')

    browser.save_screenshot(file)
    browser.close()


with open('file.csv') as csvfile:
    #opens csv file, where list of URLs exist
    reader=csv.reader(csvfile)

    for i in csvfile:
        try:
            url = i.strip()
            #strip required to delete the '\n' that randomly appears at end of variable
            selenium_out()
        except Exception as e:
            print(f"There was an error with {i}")
            #very basic exception handling


csvfile.close()
print("Script finished!")
