from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
from fold_to_ascii import fold

host = 'https://en.wiktionary.org'

def parse(url, out):
	html = urlopen(url)
	bs = BeautifulSoup(html, "html.parser")

	page = ''	
	for link in bs.find_all('a', href=re.compile('pagefrom=')):
		if 'href' in link.attrs:
			newPage = host + link.attrs['href']
			if page != newPage and newPage.find('#mw-pages') > 0:
				page = newPage
				print(page)
			
	columns = bs.findAll('div', {'class': 'mw-category-group'})
	for col in columns:
		for ul in col.find_all('ul'):
			for link in ul.find_all('a'):
				if 'title' in link.attrs:
					if link.attrs['title'].find(':') == -1:
						out.append(fold(link.attrs['title']))
	if page != '':
		print('new parse')
		print(page)
		time.sleep(1)
		parse(page, out)

lastNames = []		
parse("https://en.wiktionary.org/wiki/Category:Polish_surnames", lastNames)

# with open('ln.txt', 'w+') as f:
# 	# write elements of list
# 	for items in lastNames:
# 		f.write('%s\n' %items)

# 	print("File written successfully")
