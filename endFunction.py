def endSequence(winner, loser):
	print loser + " loses! " + winner + " is the Champion!"
	playAgain = (raw_input("Play again? Y/N >")).lower()
	if playAgain == "y":
		print "New Battle!"
		return True
	else:
		print "Game Over"
        return False
