import requests
import pandas as pd
from functools import partial
from datetime import date
import time
import os

#Pass your own API credentials in here
username = os.environ.get('EMAIL')
key = os.environ.get('SECRET_PW')

auth = (username, key)
base_url = 'https://api.passivetotal.org'

#used to save unique csv file name
date = date.today()
time = time.strftime("%H%M%S")

main = pd.DataFrame() # main dataframe. Begins as an empty df before first call appends results


def csv(csvfile):
    # Opens CSV and returns list of domains
    with open(csvfile, 'r') as csv_file:
        domains = [str(domain).strip() for domain in csv_file]
    return domains


def loop(domain, result):
    # return dataframe from json 'result' file
    item = result['results']
    spreadsheet = pd.DataFrame(item)
    spreadsheet.index = [domain] * len(spreadsheet)
    return spreadsheet


def passivetotal_get(path, query):
    url = base_url + path
    data = {'query': query, 'direction': 'children'} #important that this is 'children' or 'parent'
    # Important: Specifying json= here instead of data= ensures that the
    # Content-Type header is application/json, which is necessary.
    response = requests.get(url, auth=auth, json=data)
    # This parses the response text as JSON and returns the data representation.
    return response.json()

def makeapicall(domain):
    get_dns_passive = partial(passivetotal_get, '/v2/host-attributes/pairs')
    pdns_results = get_dns_passive(domain) #Make api call for JSON response
    df = loop(domain, result=pdns_results) # create dataframe
    return df


if __name__ == "__main__":
    domains = csv(csvfile='[name].csv') # point this to the csv file in your virtual environment you're using
    for i in range(len(domains)):
        try:
            df = makeapicall(domains[i])
            if main.empty is True:
                main = main.append(df)
            else:
                main = pd.concat([main, df])
        except UnboundLocalError as e: # exception just ignores errors, and passes on to next iteration
            print(f"There was an error processing: {i} of {e} error raised")

    main.to_csv(f'hostpair_{date}_{time}.csv')
    print("Script finished!")
