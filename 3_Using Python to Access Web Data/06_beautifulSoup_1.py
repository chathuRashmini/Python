import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
strsoup = str(soup)
info = json.loads(strsoup)

tot = 0
for item in info['comments']:
    tot = tot + item['count']
print(tot)
