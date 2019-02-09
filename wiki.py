
from bs4 import BeautifulSoup
import requests

url ="https://en.wikipedia.org/wiki/Deep_learning"
source_code = requests.get(url)
print(source_code)
plain_text = source_code.text


soup = BeautifulSoup(plain_text, "html.parser")

print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))
