import urllib.parse as urlparse
import requests
import json
import pprint
from bs4 import BeautifulSoup

course = 'csc384'
def generate_url(course):
    return urlparse.urljoin('https://markus.teach.cs.toronto.edu', course+'-2018-05/?locale=en')


url = generate_url(course)


headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 " +
                          "(KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
            'X-Requested-With': 'XMLHttpRequest',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
        }

s = requests.Session()
# s.verify = False

s.get(url)
csrftoken = s.cookies['markus-' + course + '-2018-05']
_id = {"user_login": 'chenmi84', "user_password": "6966xx511", "commit": "Log in", "authenticity_token": csrftoken}


response = s.post(url, data=_id, headers=headers)

# r = s.post("https://markus.teach.cs.toronto.edu/csc384-2018-05/en/assignments", headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
for i in soup.find("tbody").find_all('tr'):
    print(i)
    print("=" * 50)



