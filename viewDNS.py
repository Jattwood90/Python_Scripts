import pandas as pd
import json
import csv
import requests

"""Script written to automate searching of IP to domain pairings, using ViewDNS's paid API
Results are processed through a Pandas df, before exported to a spreadsheet"""


def main(file, url, apikey):
    with open('file') as csvfile: 
        reader=csv.reader(csvfile)
        csvdata=list(reader)
    spreadsheet= pd.DataFrame(columns=['ip', "hostname", "last_seen"])
    
    for index, ipaddress in enumerate(csvdata):
        try: 
            response = requests.get(url=url, params={
                'host': ipaddress, 
                'apikey': apikey,
                'output': "json" }).json()

        except UnboundLocalError as e: 
            print(f"{e} error occurred")
        
        for i, value in enumerate(response['response']['domains']): 
            spreadsheet.loc[i * index] = [ipaddress, value['name'], value['last_resolved']]
        print(spreadsheet)

if __name__ == '__main__':
    main("./test.csv", "https://api.viewdns.info/reverseip/" , "secret_api_key")
