#!/usr/bin/env python
from requests import session
from bs4 import BeautifulSoup

USER = 'nikhiledu'
PASSWORD = 'diiiiiii'

URL1 = 'https://github.com/session'
URL2 = 'https://github.com/gggg/users/graphs/traffic-data'


with session() as s:

    req = s.get(URL1).text
    html = BeautifulSoup(req)
    token = html.find("input", {"name": "authenticity_token"}).attrs['value']
    com_val = html.find("input", {"name": "commit"}).attrs['value']        

    login_data = {'login': USER,
                  'password': PASSWORD,
                  'commit' : com_val,
                  'authenticity_token' : token}

    r1 = s.post(URL1, data = login_data)
    r2 = s.get(URL2)

    Cut1 = r2.text.split(',"summary":{"total":',2)

    ViewsTot = Cut1[1].split(',"unique":',1)
    ViewsUnq = ViewsTot[1].split('}}',1)
