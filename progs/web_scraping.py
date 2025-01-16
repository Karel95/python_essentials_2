import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup # install BeautifulSoup4


# free software library BeautifulSoup from crummy.com and from pypi (beautifulsoup4)

url = input('Enter - ') # http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
