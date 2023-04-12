import requests
from bs4 import BeautifulSoup

def parse_articles():
	authors = []
	titles = []
	page = requests.get('https://hbr.org/the-latest')
	soup = BeautifulSoup(page.text, 'html.parser')
	title_h3_list = soup.find_all('h3', class_='hed')
	author_list = soup.find_all('ul', class_='byline byline-list')
	print(author_list)
	for auth in author_list:
		author = auth.find('li')
		authors.append(author.text.strip())
	for link in title_h3_list:
		title = link.find('a')
		titles.append(title.text.strip())
	return titles