from requests import get
from bs4 import BeautifulSoup as bs
from re import findall

def URLSearch():
    with open('spreadsheet.csv', 'r') as csv_file:
        domains = [str(domain).strip() for domain in csv_file]
    return domains

def UASearch(urlObj):
    
    # Retrieve html and return it's content
    requests_ret = get(urlObj).content
    bs_obj = bs(requests_ret)
    
    # Put's together a regex to search within the page's source code and extract just the UA's content
    regex = r'\'(UA.+?)\''
    
    # Uses regex findall function to search for the regex string inside the page's head tag
    ua = findall(regex, bs_obj.head.script.text)
    return ua


def listCheck(domains):
    listFound = {}
    for url in domains:
        ua = UASearch(url)
        if ua != None:
            listFound[url] = ua
    return listFound
        
            
if __name__ == '__main__':
    domains = URLSearch('spreadsheet.csv')
    print(listCheck(domains))