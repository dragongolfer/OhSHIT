# 6/9/2015
# OhSHIT! Game
#
# devCodeCamp - Brookfield, WI
# Team Helium

from playerClass import *
from time_test import *
#from user_control import *

import random
import os




#################################
# Game Initialization Functions #
#################################
def requestPlayerName(playerNumber):
    playerName = raw_input("Player " + str(playerNumber) + " -- what is your name? - ")
    return playerName


def requestPlayerType(availableCharacters):
    print("Which character do you want to play?")
    print availableCharacters
    playerType = raw_input("-- ")
    if playerType in availableCharacters:
        return playerType
    else:
        print("Sorry, that's not a valid character. Please pick from the list above.")
        return requestPlayerType(availableCharacters)


############################
# Screen Display Functions #
############################
def clearScreen():    
    os.system('cls')
        
    return

def printScoreBoard(playerList):
    pass
    return

def printWinnerScreen():
    pass
    return
    
def printGameOverScreen():
    pass
    return
    
def debug(message):
    DEBUG = False
    if DEBUG:
        print(">>DEBUG: " + str(message))
    return
    
################################
# Game Engine Helper Functions #
################################

def checkForDeath(playerList):
    for each in playerList:
        if each.get_health() < 0:
            return True
    return False

def requestWeaponChoice(player):
    options = player.get_weapons()
    weapon = readInput('Please select a weapon ', 'Ruler Slap')
    if weapon in options:
        return weapon
    else:
        print("Sorry, that is not an available option, please select one from the list above:")
        return requestWeaponChoice(player)

    
def requestPowerupChoice(player):
    options = player.get_powerups()
    powerUp = readInput('Do you want to use a powerup? ', '')
    if powerUp in options or powerUp == "":
        return powerUp
    else:
        print("Sorry, that is not an available option, please select one from the list above:")
        return requestPowerupChoice(player)
###function below from endFunction.py
def endSequence(winner, loser):
    print loser + " loses! " + winner + " is the Champion!"
    playAgain = (raw_input("Play again? Y/N >")).lower()
    if playAgain == "y":
        print "New Battle!"
        return True
    else:
        print "Game Over"
        return False


###############
# Game Engine #
###############

def main():
    availableCharacters = ["granola","notebook","backpack","computer"]

    #Play Again Loop. First match is pre-set to True.
    playAgain = True
    needToInitializePlayers = True
    winner = []
    loser = []
    while playAgain:
        playAgain = False
        
        #Initialize players
        if needToInitializePlayers:
            playerList = []
            for i in range(0,2):
                playerName = requestPlayerName(i+1)
                playerType = requestPlayerType(availableCharacters)
                player = Player(playerName,playerType)
                playerList.append(player)
                
        
        #Set Players to full health
        for each in playerList:
            each.setFullHealth()
            
        #Choose who goes first (at random)
        activePlayerIndex = random.randint(0,1)


        
        ##################
        # Main Game Loop #
        ##################
        gameOver = False
        while not gameOver:
            debug("Main loop running")
            ActivePlayer = playerList[activePlayerIndex]
            DefendingPlayer = playerList[1-activePlayerIndex]

            #Choose Weapon
            clearScreen()
            print(ActivePlayer.get_name() +", it's your turn! You have these weapons available.")
            print(ActivePlayer.get_weapons())
            weapon = requestWeaponChoice(ActivePlayer)

            #Choose Powerup
            print(ActivePlayer.get_name() +", you have these power ups available.")
            print(ActivePlayer.get_powerups())
            powerUp = requestPowerupChoice(ActivePlayer)
            if powerUp != "":
                ActivePlayer.use_power_up(powerUp)
            
            #Make Attack
            attackDamage = ActivePlayer.attack(weapon)

            #Adjust Health of opponent
            DefendingPlayer.damagePlayer(attackDamage)
            
            #Display Scoreboard
            printScoreBoard(playerList)
            
            #Check Players if either are dead
            gameOver = checkForDeath(playerList)
            if gameOver:
                winner.append(ActivePlayer)
                loser.append(DefendingPlayer)
                debug("Appending to Winner/Loser List")

            #Next Player
            activePlayerIndex = 1-activePlayerIndex


        ###############
        # End of Game #
        ###############

        # Print Winner Screen
        playAgain = endSequence(winner[-1].get_name(), loser[-1].get_name())
    
    debug(str(winner[0].get_name()))
    debug(str(loser[0].get_name()))
    return winner, loser

        
if __name__ == "__main__":
    
    main()
