# 6/9/2015
# OhSHIT! Game
#
# devCodeCamp - Brookfield, WI
# Team Helium

import Player from playerClass.py
import random



#################################
# Game Initialization Functions #
#################################

#request player character choice

#set/reset player healths(?)





############################
# Screen Display Functions #
############################
def printStartUpScreen():
    pass
    return
    
def printRules():
    pass
    return
    

    
################################
# Game Engine Helper Functions #
################################

def checkForDeath(playerList):
    pass
    return False



def main()
    ###################
    # Initialize Game #
    ###################
    printStartUpScreen()
    printRules()

    #Initialize players
    playerList = []
    for i in range(0,2):
        player = Player("granola")
        playerList.append(player)
        ##Set Player to full health
        
    #Choose who goes first (at random)
    activePlayerIndex = random.randint(0,1)

    





    ##################
    # Main Game Loop #
    ##################
    gameOver = false
    while not gameOver:
        ActivePlayer = playerList[activePlayerIndex]
        DefendingPlayer = playerList[1-activePlayerIndex]
        

        #Choose Weapon
        weapon = ActivePlayer#.selectWeaponMethod()

        #Choose Powerup
        powerUp = ActivePlayer#.selectPowerUpMethod()
        
        #Make Attack
        attackDamage = ActivePlayer#.makeAttackMethod(weapon, powerUp)

        #Adjust Health of opponent
        DefendingPlayer.#adjustHealthMethod(attackDamage)
        
        #Display Scoreboard
        printScoreBoard(playerList)
        
        #Check Players if either are dead
        gameOver = checkForDeath(playerList)
        



    ###############
    # End of Game #
    ###############

    # Print Winner Screen
    
    # Print Game Over Screen
    
    # Play again?
    # Same characters?











main()