from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

html_text = requests.get('https://www.nycgovparks.org/facilities/skateparks', headers=headers).text

soup = BeautifulSoup(html_text, 'lxml')

skateparks = soup.find('div', class_='tab-content')

skatepark_names = skateparks.find_all('h3')
skatepark_addresses = skateparks.find_all('p', class_='address')

#print(skateparks)