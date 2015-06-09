#Import libraries we need
import sys
import random

#Declare any variables we might need


#build the class 
class user_control:
	def __init__(self):
		self.game_running = True #This statement will be in a (while game_running) loop that is basically the game, to end the game just set to false
		self.quit = "Giving up so soon puny human? \n See you soon!"
		self.game_logic = None #This is where the main game function will go to be called upon initalization and start the game

	def spin_up(self):
		ye_or_ne = str(raw_input("Would you like to play OHShit!?! [ye or ne] >> "))
		decision = None
		if ye_or_ne.lower() == "ye":
			while self.game_running:
				decision = self.terminal()
				if decision == "1":
					char_stats = raw_input("What characters stats would you like to see? >>")
					#pass this input into the function that calls up the characters stats
					#blank for now, function needs to be built
				elif decision == "2":
					print "rules"
					# build a function that contains a list of all the rules and call it if this option is selected
				elif decision == "3":
					print "Starting the game"
					#call the function that initalizes the game here
				elif decision == "4":
					print "Here are the scores from the last game played"
					#print the previous game scores from an array that saves them as long as the program is running
				elif decision == "5":
					self.quitter() #this will print the quit message and end the program
				elif decision == "6":
					print "You fell for it hahahahhahaha"
		else:
			self.quitter()

	def quitter(self):
		print self.quit
		self.game_running = False

	def terminal(self):
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
			decision = str(raw_input("^>> "))
			return decision

uc = user_control()
uc.spin_up()