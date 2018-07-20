#compiling content into paragraphs
import json
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as LH
import requests
from io import StringIO


import json

reports = []
with open('bigfoot_data.json') as f:
    for i in f:
        reports.append(json.loads(i))


content_list = []
data = pd.read_json('bigfoot_data.json', lines='true',orient='records')
for i in range(1):
    soup = BeautifulSoup(reports[i]['html'], 'html.parser')



    #soup = BeautifulSoup(data['html'])

    tables = pd.read_html(data.iloc[i,1])
    content = tables[3][0][0]
    content_list.append(content)
