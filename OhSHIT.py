# 6/9/2015
# OhSHIT! Game
#
# devCodeCamp - Brookfield, WI
# Team Helium

from playerClass import Player
import random



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
def printStartUpScreen():
    pass
    return
    
def printRules():
    pass
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




def main():
    ###################
    # Initialize Game #
    ###################
    printStartUpScreen()
    printRules()
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
        printWinnerScreen()
        
        # Print Game Over Screen
        printGameOverScreen()
        
        # Play again?
        playAgain #= Play Again Function
        
        # Same characters?
        sameCharacters #= Same Characters Question Function









DEBUG = True
main()