import requests
from bs4 import BeautifulSoup
import re
import time

db = pymongo.MongoClient().local

header= {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36'}

credentials = {'username':'YOURUSERNAME','password':'YOURPASSWORD'}#EDIT HERE

okc = requests.Session()

login = okc.post('https://www.okcupid.com/login',data=credentials,headers=header)

def findPeople(searchURL):
	searchPage = okc.get(searchURL)

	soup = BeautifulSoup(searchPage.text)

	counter = 0

	for detail in soup.find_all(class_="match_card_text"):
	
		profile = detail.find('a').get('href')
		profileUsername = profile[profile.index('e/')+2:profile.index('?')]
		
		try:
			url =  "http://www.okcupid.com/profile/"+ profileUsername
			profile = okc.get(url)
			print profileUsername,'\t\t',u'\u2713'
			counter+=1
			time.sleep(3)#don't kill the okc servers, don't change this
		except:
			pass
		
	print "\n\n\n"
	print "Visited "+str(counter)+" profiles."
	print "\n\n\n"

#search url
match = "http://www.okcupid.com/match?filter1=0,34&filter2=2,24,28&filter3=3,100&filter4=5,604800&filter5=1,1&locid=0&timekey=1&matchOrderBy=MATCH&custom_search=0&fromWhoOnline=0&mygender=m&update_prefs=1&sort_type=0&sa=1&using_saved_search=&count=604800"

findPeople(match)