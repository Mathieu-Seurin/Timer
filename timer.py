#==============
"""TIMER PROJECT"""
#===============

from Tkinter import *
from time import time, sleep
from math import ceil, floor
import pygame

from app import *
from tools import *

def main():

	app = App_timer()
	app.title("Swaggatimer")
	pygame.init()
	app.mainloop()

if __name__ == "__main__":
	main()








    

