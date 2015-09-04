import random

# Code base to run the candy game played in the first 188 discussion.
#
# Each player can either take 1 or 2 candies each turn.
#
# The player who takes the last candy loses.

startPieces = 10
totalGames = 0
totalGameHistory = {}
currentGameHistory = {}
totalWins = 0

def startGame(games, pieces, aiTurn, strategy):
	play(games, pieces, aiTurn, strategy)

def play(games, pieces, aiTurn, strategy):
	global totalGameHistory, currentGameHistory, totalGames, totalWins
	if (games <= 0):
		result = input("d(data) or kp(keep playing)?")
		if (result == "d"):
			showData()
			return
		elif (result == "kp"):
			numGames = input("How many more games?")
			return startGame(numGames, startPieces, aiTurn, strategy)

	while (pieces > 0):
		if (aiTurn):
			numTaken = aiPlay(pieces)
			currentGameHistory[pieces] = numTaken
			pieces = pieces - numTaken
		else:
			pieces = pieces - strategyPlay(pieces, strategy)
		switchTurn(aiTurn)

	winner = aiTurn
	print winner

	for numPieces in currentGameHistory:
		numTaken = currentGameHistory[numPieces]

		if (numPieces not in totalGameHistory):
			totalGameHistory[numPieces] = [0, 0]

		if (winner):
			if (numTaken == 1):
				totalGameHistory[numPieces] = [totalGameHistory[numPieces][0] + 1, totalGameHistory[numPieces][1]]
			else:
				totalGameHistory[numPieces] = [totalGameHistory[numPieces][0], totalGameHistory[numPieces][1] + 1]

	if (winner):
		totalWins += 1

	currentGameHistory = {}
	totalGames += 1
	play(games - 1, startPieces, randomTurn(), strategy)

def randomTurn():
	num = random.random()
	if (num > .5):
		return 1
	return 0

def showData():
	print ("Total number of wins: " + str(totalWins))
	for key, value in totalGameHistory.iteritems():
		print key
		print value

def switchTurn(player):
	player = 1 - player

def aiPlay(pieces):
	if (pieces == 1):
		return 1
	if (pieces == 2):
		return 1
	elif (pieces == 3):
		return 2
	if (totalGames <= 300):
		num = random.random()
		if (num > .5):
			return 1
		else:
			return 2
	else:
		moveList = totalGameHistory[pieces]
		if (moveList[0] > moveList[1]):
			return 1
		return 2
	return 2

def strategyPlay(pieces, strategy):
	if (strategy == "takeTwo"):
		return 2
	if (strategy == "takeOne"):
		return 1
	if (strategy == "opposite"):
		return 1


if __name__ == '__main__':
	startGame(500, 10, 0, "takeTwo")


