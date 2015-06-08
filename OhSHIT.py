"""
class Dice:
	def __init__(self, sides):
		self.sides = sides

	def set_sides(self):
		return self.sides
"""
"""
class Fucks_Given:
	Fuck_Counter = 0
	def __init__(self, fucks):
		self.fucks = fucks

	def add_fucks(self):
		Fuck_Counter = Fuck_Counter + 1
		return Fuck_Counter

	def rem_fucks(self):
		Fuck_Counter = Fuck_Counter - 1
		return Fuck_Counter

	def get_fucks(self):
		return self.fucks
"""

"""
class Computer:
	def __init__(self, brand, processor, ram, disk):
		self.brand = brand
		self.processor = processor
		self.ram = ram
		self.diskspace = disk

	def sel_brand(self, brand):
		return sel_brand

	def sel_processor(self, processor):
		return sel_processor

	def sel_ram(self, ram):
		return sel_ram

x = Computer("Dell", "Intel", "16", "1tb")
print x.brand, x.processor, x.ram, x.diskspace
"""
#This is where the code actually starts, the others are examples I made
class Player:
	def __init__(self, weapons):
		self.health = 100
		self.weapons = []
		self.power_up_avaliable = []
		self.armor_active = True/False
		self.power_active
		self.hit

class Computer(Player):




"""
#Pygame test for reading input
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_mode((200,200))

while True:
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        if event.type == KEYDOWN:
            print event.dict['key']
            print 'break'
    pygame.event.pump()
"""
