from tkinter import *

class Application:
	def __init__(self, master=None):
		self.root = Tk()
		self.menu = Menu(self.root)
		self.root.config(menu = self.menu, bg = '#669999')
		self.fontepadrao = ("Courier new", "10")
		#self.corpadrao = '#e0ebeb'
		self.corpadrao = 'white'
		self.corclick = '#669999'

		self.button_dict = Button(self.root, text = 'Dicionário')
		self.button_dict.grid(row = 0, column = 0)	
		#self.button_dict.pack(side = TOP, padx = 50, pady = 0)	
		self.button_dict.menu = Menu(self.button_dict, tearoff = 0)
		#self.button_dict["menu"] = self.button_dict.menu
		self.button_dict["width"] = 42
		self.button_dict["height"] = 2
		self.button_dict["bd"] = 0
		self.button_dict["bg"] = self.corpadrao
		self.button_dict["activebackground"] = self.corpadrao
		self.button_dict["font"] = self.fontepadrao
		self.button_dict["command"] = self.dict_clicado

		self.button_setup = Button(self.root, text = 'Configurações')
		self.button_setup.grid(row = 0, column = 1)
		#self.button_setup.pack(side = TOP)
		self.button_setup.menu = Menu(self.button_setup, tearoff = 0)
		#self.button_setup["menu"] = self.button_setup.menu
		self.button_setup["width"] = 42
		self.button_setup["height"] = 2
		self.button_setup["bd"] = 0
		self.button_setup["bg"] = self.corpadrao
		self.button_setup["activebackground"] = self.corpadrao
		self.button_setup["font"] = self.fontepadrao
		self.button_setup["command"] = self.setup_clicado
		
		self.button_help = Button(self.root, text = 'Ajuda')
		self.button_help.grid(row = 0, column = 2)
		#self.button_help.pack( padx = 5, pady = 5)
		self.button_help.menu = Menu(self.button_help, tearoff = 0)
		#self.button_help["menu"] = self.button_help.menu
		self.button_help["width"] = 42
		self.button_help["height"] = 2
		self.button_help["bd"] = 0
		self.button_help["bg"] = self.corpadrao
		self.button_help["activebackground"] = self.corpadrao
		self.button_help["font"] = self.fontepadrao
		self.button_help["command"] = self.help_clicado

		self.button_about = Button(self.root, text = 'Sobre')
		self.button_about.grid(row = 0, column = 3)
		#self.button_about.pack(side = TOP)
		self.button_about.menu = Menu(self.button_about, tearoff = 0)
		#self.button_about["menu"] = self.button_about.menu
		self.button_about["width"] = 42
		self.button_about["height"] = 2
		self.button_about["bd"] = 0
		self.button_about["bg"] = self.corpadrao
		self.button_about["activebackground"] = self.corpadrao
		self.button_about["font"] = self.fontepadrao
		self.button_about["command"] = self.about_clicado

		self.root.mainloop()
	#Clicked button:
	def dict_clicado(self):
		self.button_dict["bg"] = self.corclick
		self.button_dict["activebackground"] = self.corclick
		self.button_setup["bg"] = self.corpadrao
		self.button_setup["activebackground"] = self.corpadrao
		self.button_help["bg"] = self.corpadrao
		self.button_help["activebackground"] = self.corpadrao
		self.button_about["bg"] = self.corpadrao
		self.button_about["activebackground"] = self.corpadrao

	"""
		self.container01 = Frame(master)
		self.container01["pady"] = 50
		self.container01["bg"] = 'black'
		self.container01.pack()
	"""

	def setup_clicado(self):
		self.button_setup["bg"] = self.corclick
		self.button_setup["activebackground"] = self.corclick
		self.button_dict["bg"] = self.corpadrao
		self.button_dict["activebackground"] = self.corpadrao
		self.button_help["bg"] = self.corpadrao
		self.button_help["activebackground"] = self.corpadrao
		self.button_about["bg"] = self.corpadrao
		self.button_about["activebackground"] = self.corpadrao

	def help_clicado(self):
		self.button_help["bg"] = self.corclick
		self.button_help["activebackground"] = self.corclick
		self.button_dict["bg"] = self.corpadrao
		self.button_dict["activebackground"] = self.corpadrao
		self.button_setup["bg"] = self.corpadrao
		self.button_setup["activebackground"] = self.corpadrao
		self.button_about["bg"] = self.corpadrao
		self.button_about["activebackground"] = self.corpadrao

	def about_clicado(self):
		self.button_about["bg"] = self.corclick
		self.button_about["activebackground"] = self.corclick
		self.button_dict["bg"] = self.corpadrao
		self.button_dict["activebackground"] = self.corpadrao
		self.button_setup["bg"] = self.corpadrao
		self.button_setup["activebackground"] = self.corpadrao
		self.button_help["bg"] = self.corpadrao
		self.button_help["activebackground"] = self.corpadrao
Application()