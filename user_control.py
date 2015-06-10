#Import libraries we need
import sys
import random
import os
from OhSHIT import *

#Declare any variables we might need


#build the class 
class user_control:
	def __init__(self):
		self.game_running = True #This statement will be in a (while game_running) loop that is basically the game, to end the game just set to false
		self.quit = "Giving up so soon puny human? \nSee you soon!"
		self.game_logic = None #This is where the main game function will go to be called upon initalization and start the game

	def spin_up(self):
		ye_or_ne = str(raw_input("Would you like to play OHShit!?! [ye or ne] >> "))
		decision = None
		if ye_or_ne.lower() == "ye":
			while self.game_running:
				decision = self.terminal()
				if decision == 1:
					self.clear()
					print "\n"
					char_stats = raw_input("What characters stats would you like to see? >>")
					#pass this input into the function that calls up the characters stats
					#blank for now, function needs to be built
				elif decision == 2:
					self.clear()
					print "\n"
					self.rules()
					print "\n"
					#function built, lists rules
				elif decision == 3:#This works
					self.clear()
					print "Starting the game"
					main()
					#main starts the game
				elif decision == 4:
					print "Here are the scores from the last game played"
					#print the previous game scores from an array that saves them as long as the program is running
				elif decision == 5:#quits the game
					self.clear()
					self.quitter() 
					#this will print the quit message and end the program
				elif decision == 6:
					print "You fell for it hahahahhahaha"
				#elif decision == 7:
		else:
		    self.quitter()


	def quitter(self):#function that quits the game
		print self.quit
		self.game_running = False

	def rules(self):#contains the rules
		print "-These are the rules of OHShit! \nNow dont fuck up as you humans often do."
		print "-Each Player(you incase you didnt get that part) \nenters their name and selects their characters"
		print "-Each character can be used multiple times \nEx: granola vs granola"
		print "-The starting health is 100 points, and you have to choose your weapon"
		print "-Careful though, because not all weapons are the same(see stats if you want idgaf)"
		print "-Make sure you choose quickly, there is a time limit \non coice or you have to use the standard weapon to fight"
		print "-And I dont like your odds in the first place \nyou need all the help you can get"
		print "-Thats why there are powerups! USE THEM! AND WISELY"
		print "-ENJOY, dont fuck up too bad."


	def clear(self):#clears the screen
		os.system("cls")
		return

	def terminal(self):#displays the main menu
		terminal = True
		while terminal:
			print "Welcome to OHShit!"
			print "The weird game where a granola bar can fight a CPU!"
			print "<1> Would you like to see the characters and their stats?"
			print "<2> Or would you like to see the complete list of rules?"
			print "<3> Play the game, and select your characters."
			print "<4> Or you can view the scores from the previous game"
			print "<5> Quit the game"
			print "<6> ???"
			print "\n"
			try:
				decision = raw_input("^>> ")
				decision = int(decision)
				return decision
			except ValueError:
				print "\nThat is not currently a valid choice broheim, try again \nand lets see if you get it right!\n"


"""This is where the various stat menus will populate and generate from 
	def sub_menu(self):
		stat_menu = True
		while stat_menu:
			print "These are dem stats you asked for"
			print "character stats"
"""
            
if __name__ == "__main__":
    ui = user_control()
    ui.spin_up()

