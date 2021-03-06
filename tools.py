from Tkinter import *
from time import time, sleep
from math import ceil, floor
import pygame
#===============================================================================================
class Passing_time(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)

		self.pack()
		self.sys_pause = False
		self.was_paused = False
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

#==============================================================================================
class Stopwatch(Passing_time):

	def __init__(self, master=None):
		Passing_time.__init__(self,master)

		self.last_bip = 0
		self.number_bip = 1
		self.bip_time = IntVar()

		self.bip_time_entry = Entry(self, textvariable=self.bip_time)
		self.bip_reset = Button(self, text="BIP", command=self.reset_bip)
		self.start_button = Button(self, text="START", command=self.preprocess)
		self.continue_button = Button(self, text="CONTINUE", command=self.continue_)

		self.timer.pack(side=TOP, expand=YES)
		self.start_button.pack()
		self.bip_reset.pack()
		self.reset_button.pack()
		self.pause_button.pack()
		self.continue_button.pack()
		self.bip_time_entry.pack()
		self.back_button.pack()
	
	def reset_bip(self):
		self.last_bip = time()
		self.number_bip = 1

	def continue_(self):
		self.sys_pause = False
		if self.reference is 0:
			self.reference = time()
			self.passed = 0
		self.stop_watch()

	def reset(self):

		self.timer['text'] = "0 : 0 : 0.0"
		self.passed = 0
		self.last_bip = 0
		self.number_bip = 1
		self.reference = 0
		self.sys_pause = True

	def preprocess(self):
		self.reset()
		self.reference = time()
		self.last_bip = time()
		self.sys_pause = False
		self.stop_watch()

	def stop_watch(self):

		if self.was_paused:
			self.was_paused = False
			self.reference = time() - self.passed 
		else:
			self.passed = time()- self.reference

		if self.sys_pause:
			self.was_paused = True
			return



		m,s = divmod(floor(self.passed),60)
		h,m = divmod(m, 60)

		ms = floor(self.passed*10 - floor(self.passed)*10)

		self.timer['text'] = "%d : %d : %d.%d" % (h,m,s,ms)
		self.update()

		if self.bip_time.get():
			lasted = time()-self.last_bip
			if lasted > self.bip_time.get():
				self.last_bip = self.reference + self.number_bip*self.bip_time.get()
				self.number_bip += 1
				##PLAY SOUND
				sound = pygame.mixer.Sound("beep.wav")
				sound.play()


		self.after(100, self.stop_watch)



#===================================================================================================	
class Timer(Passing_time):

	def __init__(self, master=None):
		Passing_time.__init__(self,master)
		self.pack()

		self.stop = IntVar()

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
			##PLAY SOUND
			son = pygame.mixer.Sound("alarm.wav")
			son.play()
			return

		m,s = divmod(floor(remain),60)
		h,m = divmod(m, 60)

		ms = floor(remain*10 - floor(remain)*10)

		self.timer['text'] = "%d : %d : %d.%d" % (h,m,s,ms)
		self.update()

	

		self.after(100, self.count_down)

		
