from tkinter import *

class Application:
	def __init__(self, master = None):
		self.root = Tk()
		self.menu = Menu(self.root)
		self.root.config(menu = self.root)

		self.button = Button(self.root, text = 'teste')
		self.button.grid(row = 0, column = 0)
		self.button.menu = Menu(self.root)

		self.button02 = Button(self.root, text = 'teste02')
		self.button02.grid(row = 0, column = 1)
		self.root.mainloop()
Application()