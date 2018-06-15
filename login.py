import urllib.parse as urlparse
import requests
import json
import pprint
from bs4 import BeautifulSoup


def generate_url(course):
    return urlparse.urljoin('https://markus.teach.cs.toronto.edu', course+'-2018-05/?locale=en')


url = generate_url('csc384')
_id = json.dumps({"user_login": 'chenmi84', "user_password": "696651**1"})

headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/"
                          "537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
            'X-Requested-With': 'XMLHttpRequest',
            'Content-type': 'application/json'
        }
s = requests.Session()
s.verify = False
response = s.post(url, data=_id, headers=headers)
r = s.post("https://markus.teach.cs.toronto.edu/csc384-2018-05/en/assignments", headers=headers)
print(response)

