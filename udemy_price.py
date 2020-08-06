"""
Option to set this up in your Windows/Mac settings so the script runs everyday. This script will send you an email, if there's a flash sale on Udemy for the course
of your choice. Just insert the URL into the 'udemy' variable, and set up your environment variables to put in your gmail account details.
"""

import requests
from bs4 import BeautifulSoup
from datetime import date
import smtplib
import os

today = date.today()
udemy = 'https://www.udemy.com/course/the-data-science-course-complete-data-science-bootcamp/'
#Nice data science course I'd like to take in the future. Any course will work, just insert the link here.


def udemy_search(udemy):
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 '
    '(X11; Ubuntu; Linux x86_64; rv:52.0) '
    'Gecko/20100101 Firefox/52.0'})
    # Headers required for requests module appear as a legitimate IP making a request against the server

    response = requests.get(udemy, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #returns div container with price nested deeply
    find_price = soup.find_all("div", class_="price-text--price-part--Tu6MH "
    "udlite-clp-discount-price udlite-heading-xl")
    #extracts the price
    try:
        price = str(find_price).split('£')[1].split('<')[0]
    except Exception:
        return 'Error!'
    return price

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #login details
    server.login(os.environ['EMAIL'], os.environ['EMAIL_PW'])
    #email details
    sub = 'Discount price on Udemy course!'
    body = f'Look at the link for udemy: {udemy}'
    message = f'Subject: {sub}\n\n{body}'
    server.sendmail(os.environ['EMAIL'],
                    os.environ['EMAIL'],
                    message)
    server.quit()

if __name__ == '__main__':
    price = udemy_search(udemy)
    if float(price) < 20:
        sendMail()
        print("You've got mail!")
