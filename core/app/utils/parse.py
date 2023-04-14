import requests
from bs4 import BeautifulSoup


def parse_articles() -> list:
	titles = []
	content_links = []
	contents = []
	names = []
	objects = []
	page = requests.get('https://hbr.org/the-latest')
	soup = BeautifulSoup(page.text, 'html.parser')
	title_h3_list = soup.find_all('h3', class_='hed')
	for link in title_h3_list:
		title = link.find('a')
		titles.append(title.text.strip())
		content_links.append(title.get('href'))
	for content_link in content_links:
		article_url = 'https://hbr.org' + content_link
		article_content = requests.get(article_url)
		content_soup = BeautifulSoup(article_content.text, 'html.parser')
		authors_ul = content_soup.find('ul', class_='article-byline-list')
		if authors_ul is None:
			names.append('-')
		else:
			names.append(authors_ul.text.replace('\n', '').replace('/n', ''))
		body_article = content_soup.find('div', class_='article-body standard-content')
		if body_article is None:
			contents.append('-')
		else:
			paragraphs = body_article.find_all('p')
			content = ''
			for paragraph in paragraphs:
				content += paragraph.text.replace('\xa0', '')
			
			contents.append(content)

	for val1, val2, val3 in zip(titles, names, contents):
		obj = {val1: (val2, val3)}
		objects.append(obj)
	return objects
	