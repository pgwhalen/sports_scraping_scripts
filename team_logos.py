from bs4 import BeautifulSoup
import urllib2
import time
import re

base_url = 'http://www.sportslogos.net'
list_url = "/logos/list_by_team/"

# returns array of indexes that correspond to each team for a league
def get_logo_page_array(url):
	soup = BeautifulSoup(urllib2.urlopen(url))

	li_tags = soup.find('div', {'id':'team'}).findAll('li')

	nums = []
	for li in li_tags:
		img_url = li.a['href']
		nums.append(int(re.sub('\D', '', img_url))) # find digits in url

	return nums


# finds logos and stores them in the right folder
def get_logos(range, dir):
	for i in range:
		try:
			soup = BeautifulSoup(urllib2.urlopen(base_url + list_url + str(i) + '/'))

			team = soup.find('div',{'id':'breadcrumb'}).div.div.span.text[:-6]
			img_page_url = soup.find('div',{'class':'section'}).ul.findAll('li')[-1].a['href']
			time.sleep(2) # don't anger the internet gods

			soup = BeautifulSoup(urllib2.urlopen(base_url + '/' + img_page_url).read())
			img_url = soup.find('div',{'class':'mainLogo'}).img['src']
			extension = img_url[-4:]
			time.sleep(2)

			img = open(dir + team + extension, 'wb')
			img.write(urllib2.urlopen(img_url).read())
			img.close()
			time.sleep(2)
		except:
			print i, "failed"

# MLB
al_nums = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/53/American_League/N/logos/')
nl_nums = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/54/National_League/N/logos/')
get_logos(al_nums + nl_nums, '/home/paul/Pictures/mlb/raw/')
# NFL
nfl_nums = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/7/National_Football_League/N/logos/')
get_logos(nfl_nums, '/home/paul/Pictures/nfl/raw/')
# NHL
nhl_nums = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/1/National_Hockey_League/N/logos/')
get_logos(nhl_nums, '/home/paul/Pictures/nhl/raw/')
# NBA
nba_nums = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/N/logos/')
get_logos(nba_nums, '/home/paul/Pictures/nba/raw/')
# NCAA
#ncaa_a_to_c = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/30/NCAA_Division_I_a-c/N/logos/')
#ncaa_d_to_h = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/31/NCAA_Division_I_d-h/N/logos/')
#ncaa_i_to_m = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/32/NCAA_Division_I_i-m/N/logos/')
#ncaa_n_to_r = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/33/NCAA_Division_I_n-r/N/logos/')
#ncaa_s_to_t = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/34/NCAA_Division_I_s-t/N/logos/')
#ncaa_u_to_z = get_logo_page_array('http://www.sportslogos.net/teams/list_by_league/35/NCAA_Division_I_u-z/N/logos/')
#get_logos(ncaa_a_to_c + ncaa_d_to_h + ncaa_i_to_m + ncaa_n_to_r + ncaa_s_to_t + ncaa_u_to_z, '/home/paul/Pictures/ncaa/raw/')