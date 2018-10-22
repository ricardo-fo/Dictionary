"""
This is a simples web scrape. It's search for words you type. The code get the HTML from 
Oxford Dictionaries -> https://en.oxforddictionaries.com
Author: Ricardo Oliveira
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests

#=====================================================================
def mainLoop():
	print('-' * 50)
	print('-' * 50)
	print("\nEncontre o significado de palavras inglesas.\n")
	print("Fazendo scraping de https://en.oxforddictionaries.com :)\nDigite 'sair' para sair.\n")
	exp = 'a'
	while True:
		print('-' * 50)
		print('-' * 50)
		exp = input("\nDigite uma palavra em inglês: ")
		if exp == 'sair':
			print("\nBye :)")
			break
		URL = ErrorTest(exp) 
		if URL != None:
			print('\n')
			translator(URL)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def ErrorTest(word):
	if ' ' in word:
		word = word.replace(' ', '-')

	URL = "https://en.oxforddictionaries.com/definition/" + word
	try:
		html = urlopen(URL)
	except HTTPError as err:
		print(err)
		return None
	except URLError:
		print("Server down or incorrect domain!\n")
		return None
	except Exception:
		return None
	else:
		return URL

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def translator(site):
	page = requests.get(site, timeout = 5)
	soup = BeautifulSoup(page.content, 'html5lib')
	page.close()

	#Parent tag
	general = soup.find(class_ = "entryWrapper")

	#Taking all informations
	all_infos = general.find_all('section', attrs = {'class':'gramb'})

	for row in all_infos:
		info = row.find_all('span', attrs = {'class':["pos", "ind", "iteration", "subsenseIteration"]})
		divs = [d.get_text() for d in info]
		for i in divs:
			print(i)

#=====================================================================

mainLoop()
