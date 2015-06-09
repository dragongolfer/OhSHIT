# 6/9/2015
# OhSHIT! Game
#
# devCodeCamp - Brookfield, WI
# Team Helium

<<<<<<< HEAD
import Player from playerClass
=======
from playerClass import *
from endFunction import *
#from user_control import *
>>>>>>> 77c6d0bd81ffa248e2d46fd1f75cec29dc3d5163
import random
import os




#################################
# Game Initialization Functions #
#################################
def requestPlayerName(playerNumber):
    playerName = raw_input("Player " + str(playerNumber) + " -- what is your name? - ")
    return "ACE"


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
    if not DEBUG:
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


###############
# Game Engine #
###############

def main():
    # game = user_control()
    # game.spinUp()

    availableCharacters = ["granola","notebook","backpack","computer"]

    #Play Again Loop. First match is pre-set to True.
    playAgain = True
    needToInitializePlayers = True
    while playAgain:
        playAgain = False
        
        #Initialize players
        if needToInitializePlayers:
            playerList = []
            for i in range(0,2):
                playerName = requestPlayerName(i+1)
                playerType = requestPlayerType(availableCharacters)
                player = Player(playerType)
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
            weapon = ActivePlayer#.selectWeaponMethod()

            #Choose Powerup
            powerUp = ActivePlayer#.selectPowerUpMethod()
            
            #Make Attack
            attackDamage = ActivePlayer#.makeAttackMethod(weapon, powerUp)

            #Adjust Health of opponent
            DefendingPlayer#.adjustHealthMethod(attackDamage)
            
            #Display Scoreboard
            printScoreBoard(playerList)
            
            #Check Players if either are dead
            gameOver = checkForDeath(playerList)
            



        ###############
        # End of Game #
        ###############

        # Print Winner Screen
        endSequence(winner, loser)
        
        # Print Game Over Screen
        printGameOverScreen()
        
        # Play again?
        playAgain #= Play Again Function
        
        # Same characters?
        sameCharacters #= Same Characters Question Function

        
if __name__ == "__main__":
    DEBUG = True
    main()
