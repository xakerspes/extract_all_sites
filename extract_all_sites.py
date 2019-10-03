from bs4 import BeautifulSoup
import urllib
import re

link_of = []
links = []
for i in range(1,18):
    url = ("".join(map(str, ["https://www.uz/ru/stat/visitors/ratings?page=",i, "&per-page=100"])))
    print(url)
    html = urllib.request.urlopen(url)
    html_page = html.read()
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
import pandas as pd
df1 = pd.DataFrame(links)
df1.to_excel("output3.xlsx")
