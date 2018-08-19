#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs

def fetch_pool():
    base_req = requests.get("https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool")
    base_req.encoding = 'utf-8'
    base_res = base_req.text
    base_soup = bs(base_res,'lxml')
    
    first_seperator = (base_soup.select("div.divider-50"))[0]
    for item in first_seperator.next_siblings:
        if repr(item) == '\n':
            continue
        if repr(item) == "<h2>See also:</h2>":
            break
        print(repr(item))

