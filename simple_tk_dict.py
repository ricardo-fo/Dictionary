from tkinter import *

class Application:
	def __init__(self, master=None):
		self.font = ("Arial", "10")
		
		self.widget1 = Frame(master)
		self.widget1.pack()
		self.msg = Label(self.widget1, text="Buscar")
		self.msg.pack()
		self.caixa = Entry(self.widget1, bd=7)
		self.caixa.pack()
		self.change_text = Button(self.widget1)
		self.change_text["text"] = "Search"
		self.change_text["width"] = 10
		self.change_text["command"] = self.mudarTexto
		self.change_text.pack()

	def mudarTexto(self):
		if self.buscar():
			self.msg["text"] = self.achar() 
		else:
			self.msg["text"] = "Não encontrado"


	def getCaixa(self):
		return self.caixa.get().lower()

	def buscar(self):
		with open('dic00.txt','r') as file:
			for line in file:
				self.getCaixa()
				search = self.getCaixa()
				if search in line:
					return True
			return False
		file.close()

	def achar(self):
		with open('dic00.txt','r') as file:
			for line in file:
				self.getCaixa()
				search = self.getCaixa()
				value = line.split('/')
				if value[0] == search:
					return value[1]
		file.close()

root = Tk()
Application(root)
root.mainloop()
		