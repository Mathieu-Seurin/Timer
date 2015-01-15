from time import time, sleep
from tkinter import *
from math import ceil, floor
import winsound
from tools import *


class Passing_time(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)

		self.sys_pause = False
		self.was_paused = False
		self.stop = StringVar()
		self.passed = 0
		self.reference = 0

		self.timer = Label(self, text = "0 : 0 : 0.0")
		self.reset_button = Button(self, text="RESET", command=self.reset)
		self.pause_button = Button(self, text="PAUSE", command=self.put_pause)
		self.back_button = Button(self, text="BACK TO MENU", command=lambda : master.flip_state("menu"))

	def reset(self):

		self.timer['text'] = "0 : 0 : 0.0"
		self.passed = 0
		self.reference = 0
		self.sys_pause = True

	def put_pause(self):
		self.sys_pause = True

	
class Timer(Passing_time):

	def __init__(self, master=None):
		Passing_time.__init__(self,master)

		self.pack()

		self.ligne_amount = Entry(self, textvariable=self.stop, width=5)
		self.start_button = Button(self, text="START", command=self.preprocess)
		self.continue_button = Button(self, text="CONTINUE", command=self.continue_)


		self.timer.pack(side=TOP, expand=YES), self.ligne_amount.pack(side=TOP,expand=YES)
		self.start_button.pack()
		self.reset_button.pack()
		self.pause_button.pack()
		self.continue_button.pack()
		self.back_button.pack()

	def continue_(self):
		self.sys_pause = False
		self.count_down()

	def preprocess(self):
	
		self.reset()
		self.reference = time()
		self.sys_pause = False
		self.count_down()


	def count_down(self):

		if self.was_paused:
			self.was_paused = False
			self.reference = time() - self.passed
		else:
			self.passed = time()- self.reference

		if self.sys_pause :
			self.was_paused = True
			return

		remain = int(self.stop.get()) - self.passed

		if remain <= 0 :

			self.timer['text'] = "0 : 0 : 0.0"
			self.update()
			paused = True
			winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
			return

		m,s = divmod(floor(remain),60)
		h,m = divmod(m, 60)

		ms = floor(remain*10 - floor(remain)*10)

		self.timer['text'] = "%s : %s : %s.%s" % (h,m,s,ms)
		self.update()

	

		self.after(100, self.count_down)



class Stopwatch(Passing_time):

	def __init__(self):
		Passing_time.__init__(self, master=None)

		self.start_button = Button(self, text="START", command= lambda : self.start_chrono(self.ligne_amount.get()))
		self.continue_button = Button(self, text="CONTINUE", command=self.continue_)





	def stop_watch():

		if paused:
			paused = False
			reference = time() - passed
		else:
			passed = time()- reference

		if pause:
			paused = True
			return

		m,s = divmod(floor(passed),60)
		h,m = divmod(m, 60)

		ms = floor(passed*10 - floor(passed)*10)

		timer['text'] = "%s : %s : %s.%s" % (h,m,s,ms)
		window.update()

		window.after(100, lambda : stop_watch())

		