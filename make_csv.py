import os
import csv
import re
import pandas as pd
from bs4 import BeautifulSoup

# maps from stat name to index in tag contents
stat_idx = {'trb':21, 'ass':22, 'pts':27}

def make_csv(data_dir):
    df = pd.DataFrame(columns=['id','pts','trb','ass'])
    for fname in os.listdir(data_dir):
        print(fname.rstrip('.html'))
        text = open(os.path.join(data_dir,fname)).read()
        soup = BeautifulSoup(text, 'html.parser')
        games = soup.find_all('tr', id=re.compile('pgl_basic'))

        for game in games:
            idx = int(game['id'].lstrip('pgl_basic.'))

            pts_tag = game.contents[stat_idx['pts']]
            trb_tag = game.contents[stat_idx['trb']]
            ass_tag = game.contents[stat_idx['ass']]

            pts = int(pts_tag.contents[0])
            trb = int(trb_tag.contents[0])
            ass = int(ass_tag.contents[0])

            df = df.append(pd.DataFrame([[idx,pts,trb,ass]], columns=['id','pts','trb','ass']))
    
    df.to_csv(os.path.join('data','log.csv'), index=False)


if __name__ ==  '__main__':
    data_dir = 'data'
    make_csv(data_dir)