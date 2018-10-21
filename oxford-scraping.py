"""
This is a simples web scrape. It's search for words you type. The code get the HTML from 
Oxford Dictionaries -> https://en.oxforddictionaries.com
Author: Ricardo Oliveira
"""

from bs4 import BeautifulSoup
import requests

def linha():
	print('-' * 50)

def translator(word):
	if(' ' in word):
		word = word.replace(' ', '-')

	#Download HTML files
	URL = "https://en.oxforddictionaries.com/definition/" + word
	page = requests.get(URL, timeout = 5)
	soup = BeautifulSoup(page.content, 'html5lib')
	page.close()

	if(page.status_code != 200):
		print("Problemas ao abrir o site!\n")
		return False

	#Parent tag
	general = soup.find(class_ = "entryWrapper")

	#Taking all informations
	infos = general.find_all('section', attrs = {'class':'gramb'})

	#Word's classes
	classes = [cl.h3.get_text() for cl in infos]

	#Taking the meanings
	i = 0
	for row in general.select('.gramb'):
		relation_tags = {}
		meanings = [mg.get_text() for mg in row.select('.ind')]
		relation_tags[classes[i]] = meanings
		print('\n', classes[i].upper())
		for j in relation_tags[classes[i]]:
			print(j)
		i = i + 1
		if i == len(classes):
			break

linha()
linha()
print("\nEncontre o significado de palavras inglesas.\n")
print("Fazendo scraping de https://en.oxforddictionaries.com :)\nDigite 'sair' para sair.\n")
exp = 'a'
while True:
	linha()
	linha()
	exp = input("\nDigite uma palavra em inglês: ")
	if exp == 'sair':
		print("Bye :)")
		break
	translator(exp)
