import requests
from bs4 import BeautifulSoup

def linha():
	print('-' * 50)

def translator(word):
	URL = "https://en.oxforddictionaries.com/definition/" + word
	page = requests.get(URL, timeout = 5)
	soup = BeautifulSoup(page.content, 'html5lib')
	table = soup.find('div', attrs = {'class':'entryWrapper'})
	print("\nResultados para " + word + ':')
	cont = 0
	for row in table.find_all('section', attrs = {'class':'gramb'}):
		cont = cont + 1
		linha()
		print(row.h3.text.upper() + ':')
		print(str(cont) + '.', row.find('span', attrs = {'class':'ind'}).text + '\n')

		#print(row.find('ol', attrs = {'class':'subSenses'}))
		if(row.find('ol', attrs = {'class':'subSenses'}) != None):
			cont2 = 0
			for line in row.find_all('li', attrs = {'class':'subSense'}):
				cont2 = cont2 + 1
				if(line.find('span', attrs = {'class':'ind'}) == None):
					break
				print(str(cont) + '.' + str(cont2),line.find('span', attrs = {'class':'ind'}).text)
		"""	
		if(row.find('ul', attrs = {'class':'semb'}) != None):
			for line in row.find_all('li'):
				print(line.find('p').text)
				print(line.find('div', attrs = {'class':'crossReference'}).text)		
		"""
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