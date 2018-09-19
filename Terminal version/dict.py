#DICTIONARY
#print("               uuuuuuu\n           uu$$$$$$$$$$$uu\n         uu$$$$$$$$$$$$$$$$$uu\n        u$$$$$$$$$$$$$$$$$$$$$u\n       u$$$$$$$$$$$$$$$$$$$$$$$u\n      u$$$$$$$$$$$$$$$$$$$$$$$$$u\n       u$$$$$$$$$$$$$$$$$$$$$$$$$u\n       u$$$$$$$$$$$$$$$$$$$$$$$$$u\n       u$$$$$$     $$$     $$$$$$u\n        $$$$       u$u       $$$$\n        $$$u       u$u       u$$$\n        $$$u      u$$$u      u$$$\n         $$$$uu$$$     $$$uu$$$$\n          $$$$$$$  .|.  $$$$$$$\n            u$$$$$$$u$$$$$$$u\n             u$ $ $ $ $ $ $u\n  uuu        $$u$ $ $ $ $u$$       uuu\n u$$$$        $$$$$u$u$u$$$       u$$$$\n  $$$$$uu       $$$$$$$$$     uu$$$$$$\nu$$$$$$$$$$$uu    ;;;;;    uuuu$$$$$$$$$$\n$$$$   $$$$$$$$$$uuu   uu$$$$$$$$$   $$$")
exit1 = True
print("______ _      _   _                              \n|  _  (_)    | | (_)                             \n| | | |_  ___| |_ _  ___  _ __   __ _ _ __ _   _ \n| | | | |/ __| __| |/ _ \\| '_ \\ / _` | '__| | | |\n| |/ /| | (__| |_| | (_) | | | | (_| | |  | |_| |\n|___/ |_|\\___|\\__|_|\\___/|_| |_|\\__,_|_|   \\__, |\n                                            __/ |\n                                           |___/ \n")
print("P A R A   O B T E R   A J U D A   D I G I T E  ajuda")
while(exit1):
	# BUSCA GLOBAL
	search = input("\nGLOBAL>>> ").lower()
	#search = search.lower()

	# SAI DO DICIONÁRIO---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	if(search == 'sair' or search == 'sai'):
		exit1 = False
		break

	# AJUDA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	elif(search == 'ajuda' or search == 'help' or search == 'a' or search == 'h'):
		print("*************************************************************\n***                         AJUDA                         ***\n*************************************************************")
		print("\n1 - AJUDA EM ADIÇÕES;\n2 - AJUDA EM LEITURA;\n3 - AJUDA EM BUSCA;\n4 - AJUDA EM REMOÇÃO;\n5 - MAIS INFORMAÇÕES (SOBRE).\n DIGITE O NÚMERO DA AJUDA.")
		ajuda = input("\nHELP>>> ")
		if(ajuda == '1'):
			print("\n1 - AJUDA EM ADIÇÕES:\n\n1.1. ADICIONAR UMA NOVA PALAVRA\n    Para que seja adicionada uma nova palavra \nem seu dicionário, você deve digitar uma das \nalternativas abaixo:\n- novo\n- new\n- escrever\n- write\n- n\n- e\n- w\n  Após a Adição de Termos ser chamada, pede-se\npara que seja informado, primeiramente, o termo\nem inglês,após o termo em inglês ser informado,\nvocê deve dizer o significado e/ou a tradução\ndele. Para parar de adicionar novos termos,\ndigite 'sair'.")
			next01 = input(". . .")
			print("Exemplo:\n\nING>>> red\n\nPOR>>> vermelho\n\nING>>> sair\n\nGLOBAL>>> ")
			next01 = input(". . .")
			print("\n\n1.2. SEPARAÇÃO DE SIGNIFICADOS\n    Caso o termo adicionado possua mais de um\nsignificado, para separá-los, use '/' sem\nespaços. Exemplo:\n\nING>>> wall\n\nPOR>>> parede/muro/muralha\n")
			next01 = input(". . .")
			print("\n1.3. - CANCELAR UMA ADIÇÃO\n    Caso queira cancelar uma adição, deve-seescrever em 'POR>>> ' a palavra 'sair'.\n  Para sair da área de adição, digite ou 'sair'\nou 'sai'. Exemplo:\n\nING>>> marrom\n\nPOR>>> sair\n")
			next01 = input(". . .")
			print("\n1.4. - TERMOS REPETIDOS\n    Caso tente adicionar um termo repetido, uma\nmensagem informando que ele já está no dicionário\naparecerá para o auxiliar. Serão dados três opções\npara prosseguir, são estas: adicionar novos\nsignificados, substituir os significados antigos\ne a opção de cancelar a adição do termo. Exemplo:\n\nING>>> green\n\n- ESSE TERMO JÁ ESTÁ EM SEU DICIONÁRIO.\n- DESEJA SUBSTITUIR O(S) ANTIGO(S) SIGNIFICADO(S)\n(subs)\n- OU ADICIONAR NOVO(S) SIGNIFICADO(S)(ad)\n\nTERM>>>\n ") 
			next01 = input(". . .")
			print("\n     1.4.1. - ADIÇÃO\n	   Para que novos significados sejam\nadicionados sem que haja perda dos antigos,\ndeve-se digitar uma das opções abaixo para acessar\neste recurso:\n	- adicionar\n	- ad\n	- a\n	   Quando esse recurso for chamado, a seta\nindicando que deve ser adicionado significado ao\ntermo, 'POR>>> ', aparecerá. Para adicionar\nnovos significados ao termo repetido, sem excluir\nos antigos, é claro, basta digitar da mesma forma\nque é digitado quando se deseja adicionar um\ntermo não existe.")
			next01 = input(". . .")
			print("Por exemplo:\n\nING>>> green\n\n- ESSE TERMO JÁ ESTÁ EM SEU DICIONÁRIO.\n- DESEJA SUBSTITUIR O(S) ANTIGO(S) SIGNIFICADO(S)\n(subs)\n- OU ADICIONAR NOVO(S) SIGNIFICADO(S)(ad)\n\nTERM>>> adicionar\n\nPOR>>> verde/gramado\n- NOVOS SIGNIFICADOS ADICIONADOS COM SUCESSO.\n")
			next01 = input(". . .")
			print("\n\n     1.4.2. - SUBSTITUIÇÃO\n\n	    Para que novos significados sejam\nadicionados fazendo com que os antigos sumam, isto\né, substituí-los, deve-se digitar uma das opções\nabaixo para ter acesso a esse recurso:\n	- substituir\n	- subs\n	- s\n	    Quando esse recurso for chamado, a\nseta indicando que deve ser adicionado (substituído)\nsignificado ao termo, 'POR>>> ', aparecerá.Para\nsubstituir os significados do termo repetido,\ndigite da mesma forma que é digitado quando se\ndeseja adicionar um termo não existe.")
			next01 = input(". . .")
			print("Caso não\nqueira mais adicionar um novo termo, basta digitar\n'sair' para que o recurso seja cancelado. Exemplo:\n\nING>>> green\n\n- ESSE TERMO JÁ ESTÁ EM SEU DICIONÁRIO.\n- DESEJA SUBSTITUIR O(S) ANTIGO(S) SIGNIFICADO(S)\n(subs)\n- OU ADICIONAR NOVO(S) SIGNIFICADO(S)(ad)\n\nTERM>>> substituir\n\nPOR>>> verde\n\n- PALAVRA SUBSTITUIDA COM SUCESSO.\n")
			next01 = input(". . .")
			print("\n      1.4.3. - CANCELAR\n	    Para que uma modificação no termo seja\nfeita, digite 'sair'. Exemplo:\n\nING>>> green\n\n- ESSE TERMO JÁ ESTÁ EM SEU DICIONÁRIO.\n- DESEJA SUBSTITUIR O(S) ANTIGO(S) SIGNIFICADO(S)\n(subs)\n- OU ADICIONAR NOVO(S) SIGNIFICADO(S)(ad)\n\n\nTERM>>> sair\n\nGLOBAL>>> ")
			next01 = input()
		elif(ajuda == '2'):
			print("\n2 - AJUDA EM LEITURA\n\n	Para ver todos os termos que estão em seu dicionário, digite uma das alternativas abaixo:\n- ler\n- read\n- ver\n- l\n- r\n- v\n\n   O modo leitura foi feito para consultar todas\nas palavras existentes no dicionário. Isto é,\nquando esse recurso for chamado, aparecerão todos\nos termos, juntos aos seus respectivos significados,\nem uma lista. ")
		elif(ajuda == '3'):
			print("\n3 - AJUDA EM BUSCA\n\n    Para saber se algum termo está em seu dicionário, apenas digite \no termo que você será redirecionado à área de busca.\n    Caso o termo esteja em seu dicionário, abaixo desse aparecerá seu(s)\nsignificado(s). Caso não esteja, não aparecerá resultado para a busca.\n    Para sair da área de busca, digite 'sair' ou 'sai'.")
		elif(ajuda == '4'):
			print("\n3 - AJUDA EM REMOÇÃO\n\n    Para remover um termo de seu dicionário, digite uma das opções abaixo:\n- delete\n- deletar\n- excluir\n- apagar\n- del\n- d\n\n    Em seguida, digite o termo que deseja remover.\n")
		elif(ajuda == '5'):
			print("\n 	Este programa foi criado por Ricardo de Freitas, entre os dias 10/07/2018 e 16/07/2018.\nEste dicionário visa ajudar e facilitar a vida de seu usuário, trazendo mais agilidade no dia à dia.\n 	O programa inteiro foi desenvolvido individualmente, feito na linguagem Python 3.7.0.\n 	Redes sociais do criador:\n https://www.facebook.com/RicardoFreitas0\n https://twitter.com/@RicardoFoo_\n https://github.com/ricardo-fo\n")
	# ADIÇÃO---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	elif(search == 'novo' or search == 'new' or search == 'escrever' or search == 'write' or search == 'w' or search == 'n' or search == 'e'):
		print("*************************************************************\n***                   ADIÇÃO DE TERMOS                    ***\n*************************************************************")
		exit2 = True
		while(exit2):
			# OBTÊM O NOVO TERMO EM INGLÊS
			novo_ing = input("\nING>>> ").lower()
			#novo_ing = novo_ing.lower()
			exit5 = False
			if(novo_ing == 'sair' or novo_ing == 'sai'):
				exit2 = False
				break
			# CONTROLE DE REPETIÇÃO DE TERMOS
			i = 0
			while(i <= 42):
				arquivo = open('dic00.txt','r')
				for line in arquivo:
					valor = line.split('/')
					# VERIFICA SE O TERMO JÁ ESTÁ NO DICIONÁRIO
					if(valor[0] == novo_ing):
						print("\n- ESSE TERMO JÁ ESTÁ EM SEU DICIONÁRIO.\n- DESEJA SUBSTITUIR O(S) ANTIGO(S) SIGNIFICADO(S)(subs)\n- OU ADICIONAR NOVO(S) SIGNIFICADO(S)(ad)")
						print("\n- {} TEM O(S) SEGUINTE(S) SIGNIFICADO(S):".format(valor[0]))
						carac = 0
						# QUANTIFICA QUANTOS SIGNIFICADOS O TERMO POSSUI
						for caractere in line:
							if(caractere in '/'):
								carac += 1
						i = 1
						while(i < carac):
							print('-',valor[i])
							i += 1
						termo_repetido = input("\nTERM>>> ").lower()
						#termo_repetido = termo_repetido.lower()
						# USUÁRIO QUER SUBSTITUIR OS SIGNIFICADOS DO TERMO REPETIDO
						if(termo_repetido == 's' or termo_repetido == 'subs' or termo_repetido == 'substituir'):
							# OBTÉM O NOVO SIGNIFICADO
							novo_pt = input('\nPOR>>> ').lower()
							#novo_pt = novo_pt.lower()
							if(novo_pt == 'sair' or novo_pt == 'sai'):
								i = 43
								exit2 = False
								exit5 = True
								novo_ing = None
								break
							else:
								# ESCREVE O MESMO TERMO, novo_ing + novo_pt, EM UM ARQUIVO AUXILIAR
								with open('subs00.txt','a+') as file:
									file.write(novo_ing)
									file.write('/')
									file.write(novo_pt)
									file.write('/')
									file.write('\n')
									# COPIA O CONTEÚDO DO DICIONÁRIO PARA O ARQUIVO AUXILIAR COM EXCEÇÃO DO TERMO REPETIDO
									with open('dic00.txt','r') as arquivo:
										for line in arquivo:
											value = line.split('/')
											if(value[0] != novo_ing):
												file.write(line)
								# APAGA TODO O CONTEÚDO DO DICIONÁRIO
								file = open('dic00.txt','w')
								file.close()
								# RECOLOCA TODO O CONTÉUDO NO DICIONÁRIO
								with open('subs00.txt','r') as file:
									with open('dic00.txt','a+') as file01:
										for line in file:
											value = line.split()
											file01.write(line)
								# APAGA O CONTEÚDO DO ARQUIVO AUXILIAR PARA QUE ELE POSSA SER USADO FUTURAMENTE
								file = open('subs00.txt','w')
								file.close()
								print("\n- NOVOS SIGNIFICADOS SUBSTITUIDOS COM SUCESSO.")
								i = 43
								exit5 = True
								novo_ing = None
								break
						# USUÁRIO QUER ADICIONAR NOVOS SIGNIFICADOS AO TERMO REPETIDO
						elif(termo_repetido == 'a' or termo_repetido == 'ad' or termo_repetido == 'adicionar'):
							# OBTÉM OS NOVOS SIGNIFICADOS DO TERMO REPETIDO
							novo_pt = input('\nPOR>>> ').lower()
							#novo_pt = novo_pt.lower()
							if(novo_pt == 'sair' or novo_pt == 'sai'):
								novo_ing = None
								exit2 = False
								exit5 = True
								i = 43
								break
							# ABRE O ARQUIVO AUXILIAR E O ARQUIVO DICIONÁRIO, RESPECTIVAMENTE
							with open('subs00.txt','a+') as file:
								with open('dic00.txt','r') as arquivo:
									# VERIFICA TODAS AS LINHAS DO DICIONÁRIO PARA ENCONTRAR O TERMO REPETIDO
									for line in arquivo:
										value = line.split('/')
										# COPIA TUDO, COM EXCEÇÃO DO TERMO REPETIDO, PARA O ARQUIVO AUXILIAR
										if(value[0] != novo_ing):
											file.write(line)
										else:
											# CONTA QUANTOS SIGNIFICADOS O TERMO REPETIDO POSSUI
											cont = 0
											for caractere in line:
												if(caractere in '/'):
													cont += 1
											# ESCREVE TODO O CONTEÚDO DO TERMO REPETIDO NO ARQUIVO AUXILIAR
											i = 0
											while(i < cont):
												file.write(value[i])
												file.write('/')
												i += 1
											# ESCREVE OS NOVOS SIGNIFICADOS AO FINAL DO TERMO REPETIDO NO ARQUIVO AUXILIAR
											file.write(novo_pt)
											file.write('/')
											file.write('\n')
							# APAGA TODO O CONTEÚDO DO DICIONÁRIO
							file = open('dic00.txt','w')
							file.close()
							# RECOLOCA TODO O CONTÉUDO NO DICIONÁRIO
							with open('subs00.txt','r') as file:
								with open('dic00.txt','a+') as file01:
									for line in file:
										value = line.split()
										file01.write(line)
							# APAGA O CONTEÚDO DO ARQUIVO AUXILIAR PARA QUE ELE POSSA SER USADO FUTURAMENTE
							file = open('subs00.txt','w')
							file.close()
							print("- NOVOS SIGNIFICADOS ADICIONADOS COM SUCESSO.")
							exit5 = True
							novo_ing = None
							i += 1
						elif(termo_repetido == 'sair' or termo_repetido == 'sai'):
							exit2 = False
							exit5 = True
							novo_ing = None
							i = 43
							break
						else:
							print("! RESPOTA NÃO COMPREENDIDA !")
							exit5 = True
							novo_ing = None
							i = 43
							break
					else:
						i += 2
				arquivo.close()
			# OBTÉM O SIGNIFICADO DO TERMO CASO NÃO TENHA SIDO PEGO ANTERIORMENTE
			if(exit5 and novo_ing == None):
				pass
			else:
				novo_pt = input("\nPOR>>> ").lower()
				#novo_pt = novo_pt.lower()
				if(novo_pt == 'sair' or novo_pt == 'sai'):
					exit2 = False
					break
				with open('dic00.txt','a') as arquivo:
					# ADICIONA OS NOVOS TERMOS NO ARQUIVO E DIFERENCIA ELES
					arquivo.write(novo_ing)
					arquivo.write('/')
					arquivo.write(novo_pt)
					arquivo.write('/')
					arquivo.write('\n')
	# REMOVER---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	elif(search == 'del' or search == 'delete' or search == 'deletar' or search == 'apagar' or search == 'excluir' or search == 'd'):
		print("*************************************************************\n***                        EXCLUIR                        ***\n*************************************************************")
		# ENTRADA DA PALAVRA A SER DELETADA
		deletar = input('\nDEL>>> ').lower()
		#deletar = deletar.lower()
		if(deletar == 'sair' or deletar == 'sai'):
			pass
		else:
			# ABRE O ARQUIVO AUXILIAR E O DICIONARIO, RESPECTIVAMENTE
			with open('subs00.txt','a+') as file:
				with open('dic00.txt','r') as arquivo:
					# ANALISA LINHA POR LINHA DO DICIONÁRIO
					for line in arquivo:
						value = line.split('/')
						# COLOCA TODO O CONTEÚDO, COM EXCEÇÃO DA PALAVRA A SER DELETADA, DO DICIONÁRIO NO ARQUIVO AUXILIAR
						if(value[0] != deletar):
							file.write(line)
			# APAGA TODO O CONTEÚDO DO DICIONÁRIO
			file = open('dic00.txt','w')
			file.close()
			# RECOLOCA TODO O CONTEÚDO NO DICIONÁRIO
			with open('subs00.txt','r') as file:
				with open('dic00.txt','a+') as file01:
					for line in file:
						value = line.split()
						file01.write(line)
			# APAGA O CONTEÚDO DO ARQUIVO AUXILIAR PARA QUE ELE POSSA SER USADO FUTURAMENTE
			file = open('subs00.txt','w')
			file.close()
			print("\n- PALAVRA APAGADA COM SUCESSO")

	# LEITURA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	elif(search == 'ler' or search == 'read' or search == 'l' or search == 'ver' or search == 'r' or search == 'v'):
		print("*************************************************************\n***                  TODAS AS PALAVRAS                    ***\n*************************************************************")
		exit3 = True
		while(exit3):
			with open('dic00.txt','r') as arquivo:
				contador = 0
				# LÊ LINHA POR LINHA DO ARQUIVO
				for line in arquivo:
					valor = line.split('/')
					contador += 1
					cont = 0
					# PROCURA POR UM DETERMINADO CARACTERE
					for caractere in line:
						# IDENTIFICA SE HÁ TROCA DE TERMO
						if(caractere in '/'):
							cont += 1
					# IMPRIME A PALVRA EM PORTUGUÊS
					print('#',valor[0],':')
					i = 1
					# IMPRIME AS TRADUÇÕES
					while(i < cont):
						print('-',valor[i])
						i += 1
					print()
				exit3 = False
	# BUSCA---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	elif(search != 'sair'):
		print("*************************************************************\n***                     ÁREA DE BUSCA                     ***\n*************************************************************")
		exit4 = True
		while(exit4):
			arquivo = open('dic00.txt','r')
			# BUSCA LINHA POR LINHA
			for line in arquivo:
				valor = line.split('/')
				cont = 0
				# IDENTIFICA SE O TERMO ESTÁ NA LINHA
				if(search in line):
					cont = 0
					# IDENTIFICA A QUANTIDADE DE TERMOS DA LINHA
					for caractere in line:
						if(caractere in '/'):
							cont += 1
					# VERIFICA SE O TERMO É EM INGLÊS
					if(valor[0] == search):
						j = 1
						while(j < cont):
							print('-',valor[j])
							j += 1
					else:
						# SE NÃO FOR, ENTÃO SÓ PODE SER EM PORTUGUÊS
						i = 1
						for i in range(cont):
							if(valor[i] == search):
								print('-',valor[0])
								break
			arquivo.close()
			search = input("\nSEARCH>>> ").lower()
			#search = search.lower()
			# SAI DA BUSCA
			if(search == 'sair' or search == 'sai'):
				exit4 = False
		search = '*'		