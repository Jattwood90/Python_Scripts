import requests
import csv
import pandas as pd

#open csv file and export as list
def openList(filepath):
    with open(filepath, "r", encoding="utf8") as csvfile:
        reader = list(csv.reader(csvfile))
    return output

#run request search for status codes
def search(url):
    headers = requests.utils.default_headers()
    headers.update({
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/81.0.4044.122 Safari/537.36'})

    try:
        search_url = 'https://www.' + str(url).strip('[]').strip("'").strip("'") #strip required to remove annoying brackets, and quotations marks
        r = requests.get(search_url, headers=headers, timeout=5.0)
        response = r.status_code
        return response
    except:
        r = requests.exceptions.ConnectionError
        return 'error'

if __name__ == "__main__":
    filepath = 'path to csv file'
    searchList = openList(filepath)
    names = [i for i in searchList]
    status_codes = list(map(search, searchList))
    df = pd.DataFrame(list(zip(names, status_codes)))
    df.to_csv('output.csv')



