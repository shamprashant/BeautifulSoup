from bs4 import BeautifulSoup
import requests


with open('simple.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')
	# to get the whole html
	print(soup.prettify())

	# to work with title tag
	title_tag = soup.title
	print(title_tag.text)

	#to work with div tag
	div = soup.find('div', class_ = 'footer')
	print(div.text)

# to get all the div with class article
for article in soup.find_all('div', class_ = 'article'):
	heading = article.h2.a.text
	print(heading)

	summary = article.p.text
	print(summary)

	print()