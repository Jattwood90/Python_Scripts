"""
For the most part, this will mean nothing to anyone looking at this. Essentially this bot was built to automate a form fill, for over 1,000 entries.
To save my wrists and the will to live, I used Selenium to log into the system, and repeatedly fill out the form for me.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

searchterms = ["search-terms"]

csvfile = 'path to file.csv'

def csv(csvfile):
    # Opens CSV and returns list of domains
    with open(csvfile, 'r') as csv_file:
        domains = [str(domain).strip() for domain in csv_file]
    return domains


def selenium_out():
    #Long function, but was only made to brute force the form fill.
    browser = webdriver.Chrome()
    browser.get("webpage login")
    browser.maximize_window()
    #login requirements
    username = browser.find_element_by_name("email")
    username.clear()
    username.send_keys("email_address")
    #password
    password = browser.find_element_by_name("password")
    password.clear()
    password.send_keys("pw")
    #select login
    login = browser.find_element_by_tag_name('button')
    login.click()
    #navigate to source code crawler
    time.sleep(3)
    cururl = browser.current_url[:-5]
    browser.get(cururl+'source_code_search')
    #fill out source code crawler
    time.sleep(3)
    return browser

def fillDetails(browser, searchTerm):
    name = browser.find_element_by_name('name')
    name.clear()
    name.send_keys(searchTerm)

    url = browser.find_element_by_name('url')
    url.clear()
    url.send_keys('https://www.' + searchTerm)

    def search(items):
        keyterms = browser.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div[1]/div/div/div[2]/form/div[1]/div[3]/div/div[1]/input')
        keyterms.clear()
        keyterms.send_keys(items)
        keyterms.send_keys(Keys.RETURN)

    for items in searchterms:
        search(items)
        time.sleep(2)

    check = browser.find_element_by_name('fullDomainCrawl')
    check.click()

    name = browser.find_element_by_name('name')
    name.send_keys(Keys.RETURN)

    time.sleep(3)

if __name__ == "__main__":
    start_time = datetime.now()
    domains = csv(csvfile)
    count = len(domains)
    browser = selenium_out()

    for items in domains:
        try:
            fillDetails(browser, items)
            time.sleep(2)
        except Exception as e:
            print(f'There was an error with: {e}')

    print(f"Script finished! {count} number of requests processed!")
    time_taken = datetime.now() - start_time
    print(f"This script took: {time_taken} to complete")
