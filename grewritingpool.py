#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs

def fetch_pool():
    base_req = requests.get("https://www.ets.org/gre/revised_general/prepare/analytical_writing/argument/pool")
    base_req.encoding = 'utf-8'
    base_res = base_req.text
    base_soup = bs(base_res,'lxml')
    return base_soup

