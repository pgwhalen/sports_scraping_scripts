from bs4 import BeautifulSoup
import urllib2
import time

base_url = 'http://www.sportslogos.net'
list_url = "/logos/list_by_team/"

def get_logos(range, dir):
	for i in range:
		try:
			soup = BeautifulSoup(urllib2.urlopen(base_url + list_url + str(i) + '/'))

			team = soup.find('div',{'id':'breadcrumb'}).div.div.span.text[:-6]
			img_page_url = soup.find('div',{'class':'section'}).ul.findAll('li')[-1].a['href']
			time.sleep(2) # don't anger the internet gods

			soup = BeautifulSoup(urllib2.urlopen(base_url + '/' + img_page_url).read())
			img_url = soup.find('div',{'class':'mainLogo'}).img['src']
			time.sleep(2)

			img = open(dir + team + '.gif', 'wb')
			img.write(urllib2.urlopen(img_url).read())
			img.close()
			time.sleep(2)
		except:
			print i, "failed"

# MLB
get_logos(range(50, 91), '/home/paul/Pictures/mlb/')
# NFL

# NHL

# NBA

# NCAA
