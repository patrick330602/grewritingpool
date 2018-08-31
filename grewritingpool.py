#!/usr/bin/env python3

import json
import requests
from bs4 import BeautifulSoup as bs
from bs4 import element


def fetch_pool():
    base_req = requests.get("https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool")
    base_req.encoding = 'utf-8'
    base_res = base_req.text
    base_soup = bs(base_res,'lxml')

    pool = []
    first_seperator = (base_soup.select("div.divider-50"))[0]
    status = 1
    tmp = {}
    for item in first_seperator.next_siblings:
        if isinstance(item,element.NavigableString):
            continue
        elif repr(item).startswith("<h2>"):
            break
        elif status == 1 and item.name == "p":
            tmp['qfirst']  = item.contents[0]
            status = 2
        elif status == 2 and item.name == "p":
            tmp['qsecond'] = item.contents[0]
            status = 2
        elif status == 2 and item.name == "div":
            status = 3
            tmp["instru"] = item.contents[0]
        elif status == 3 and item.name == "div":
            pool.append(tmp)
            tmp = {}
            status = 1
    print(pool)