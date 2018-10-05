import codecs
import requests
from bs4 import BeautifulSoup

def nickname(word):
	html = requests.get("https://connpass.com/api/v1/event/?nickname=" + word)
	soup = BeautifulSoup(html.text, "html.parser")
	cc = codecs.decode(soup, "unicode-escape")
	print(cc)
	
	
	
	
	
	#print(soup)
	#for title in events:
		#cc = codecs.decode(title, "unicode-escape")
		#print(cc)

nickname("comet_it")
