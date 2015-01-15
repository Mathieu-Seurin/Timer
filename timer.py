#==============
"""TIMER PROJECT"""
#===============

from time import time, sleep
from tkinter import *
from math import ceil, floor
import winsound
from tools import *

class App_timer(Tk):

	def __init__(self):

		Tk.__init__(self)
		self.all_buttons = []
		self.launch_menu()


	def launch_menu(self):

		self.frame = Frame(self)
		self.frame.pack()
		self.what_to = Label(self.frame, text="WHAT DO YOU WANT TO DO ?")
		self.timer_state = Button(self.frame, text="TIMER",command=lambda : self.flip_state("timer"))
		self.stop_watch_state = Button(self.frame,text="STOPWATCH",command=lambda : self.flip_state("stopwatch"))
		self.pomodoro_state = Button(self.frame,text="POMODORO", command=lambda : self.flip_state("pomodoro"))

		self.all_buttons = [self.what_to, self.timer_state, self.stop_watch_state, self.pomodoro_state]

		for button in self.all_buttons:
			button.pack(fill=BOTH,expand=YES)

	def flip_state(self, new_state):
		
		self.frame.destroy()

		if new_state == "timer":
			self.frame = Timer(self)

		elif new_state == "stopwatch":
			self.frame = Stopwatch(self)

		elif new_state == "pomodoro":
			self.frame = Pomodoro(self)

		else:
			self.launch_menu()


def main():

	app = App_timer()
	app.title("Swaggatimer")
	app.mainloop()
if __name__ == "__main__":
	main()








    

