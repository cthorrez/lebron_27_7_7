import os
import time
import urllib.request   


def get_data():
    base = 'https://www.basketball-reference.com/players/j/jamesle01/gamelog/'
    years = [str(x) for x in range(2004,2019)]
    for year in years:
        time.sleep(1)
        url = base + year
        urllib.request.urlretrieve(url, os.path.join('data',year+'.html'))

if __name__ == '__main__':
    get_data()
