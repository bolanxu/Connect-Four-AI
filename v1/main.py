''' 
Contestant 1: Bolan Xu    			   
'''

'''
@BolanXu

AI Chat Version = 0.2
Copyright C 2023 GNU License
Bolan Xu
Submission: No. 1
'''

import random
import time
import os
import copy
from colorama import Fore
#import numpy

turn = 1

grid = [[' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ']]

AI_grid = []

class GameBoard:
	#def __init__(self,sizeX, sizeY):
	#	global grid
	#	self.sizeX = sizeX
	#	self.sizeY = sizeY
	def place(column,Player):
		#if Player == 0:
		#	color1 = Fore.RED
		#else:
		#	color1 = Fore.BLUE
		try:
			for i in range(0,6):
				if grid[i][column-1] != ' ':
					continue
				else:
					grid[i][column-1] = Player
					break
		except:
			print(f"{Fore.ORANGE}Sorry. You cannot place there.{Fore.WHITE}")
			time.sleep(2)
	def placeAI(column1,Player1):
		try:
			for i in range(0,6):
				if AI_grid[i][column1-1] != ' ':
					continue
				else:
					AI_grid[i][column1-1] = Player1
					break
		except:
			print(f"{Fore.ORANGE}Sorry. You cannot place there.{Fore.WHITE}")
			time.sleep(2)
	def cancel(column,board):
		for i in range(0,6):
			try:
				if board[5][column-1] != ' ':
					#print("Canceled grid")
					board[5][column-1] = ' '
					break
				if board[i][column-1] != ' ':
					#print(grid[5][column-1])
					continue
				else:
					board[i-1][column-1] = ' '
					break
				#print(grid[5][column-1])

			except IndexError:
				print(f"{Fore.ORANGE}Sorry. You cannot place there.{Fore.WHITE}")
				time.sleep(2)

			#print("Sorry. You cannot place there.")
			#time.sleep(2)
			#pass
	def clearBoard(board):
		for iy in range(0,len(board)):
			for ix in range(0,len(board[iy])):
				board[iy][ix] = ' '
	def fourInRow(player,board):
		for iy in range(0,len(board)):
			for ix in range(0,len(board[iy])):
				if board[iy][ix] == player:
					try:
						if board[iy+1][ix+1] == player:
							if board[iy+2][ix+2] == player:
								if board[iy+3][ix+3] == player:
									return True
						if board[iy][ix+1] == player:
							if board[iy][ix+2] == player:
								if board[iy][ix+3] == player:
									return True
						if board[iy+1][ix] == player:
							if board[iy+2][ix] == player:
								if board[iy+3][ix] == player:
									return True
						if board[iy+1][ix-1] == player:
							if board[iy+2][ix-2] == player:
								if board[iy+3][ix-3] == player:
									return True
					except IndexError:
						continue
		return False
	def threeInRow(player,board):
		for iy in range(0,len(board)):
			for ix in range(0,len(board[iy])):
				if board[iy][ix] == player:
					try:
						if board[iy+1][ix+1] == player:
							if board[iy+2][ix+2] == player:
								return True
						if board[iy][ix+1] == player:
							if board[iy][ix+2] == player:
								return True
						if board[iy+1][ix] == player:
							if board[iy+2][ix] == player:

								return True
						if board[iy+1][ix-1] == player:
							if board[iy+2][ix-2] == player:

								return True
					except IndexError:
						continue
		return False
	def twoInRow(player,board):
		for iy in range(0,len(board)):
			for ix in range(0,len(board[iy])):
				if board[iy][ix] == player:
					try:
						if board[iy+1][ix+1] == player:

							return True
						if board[iy][ix+1] == player:

							return True
						if board[iy+1][ix] == player:

							return True
						if board[iy+1][ix-1] == player:

							return True
					except IndexError:
						continue

		return False
	def copyData(board1,board2):
		#board = []
		#board2 = []
		for a in board1:
			board2.append(a)
		return board2

class AI:
	
	def canMove(column,board):
		#print(board)
		return False if board[5][column-1] != ' ' else True
	def possibleMoves():
		posMoveList = []
		for j in range(0,7):
			if AI.canMove(j,grid) == True:
				posMoveList.append(j)
			else:
				continue
		return posMoveList
	def possibleMovesAI():
		posMoveList = []
		for j in range(0,7):
			if AI.canMove(j,AI_grid) == True:
				posMoveList.append(j)
			else:
				continue
		return posMoveList
	def nextMove(player, depth):
		global AI_grid
		dropped = []
		scoreList = []
		#GameBoard.clearBoard(AI_grid)
		#AI_grid = grid
		#printGrid()
		#printGridAI()
		AI_grid = copy.deepcopy(grid)
		if player == 1:
			otherPlayer = 0
		else:
			otherPlayer = 1
		score = 0
		bestMove = 0
		bestScore = -100000
		otherScore = -100000
		#if isFirst == True:
		#	return 4
		def minimax(move, player):
			GameBoard.placeAI(move+1, player)
			#dropped.append(move+1)
			score = AI.utility(player)
			return score
		for move in AI.possibleMovesAI():
			dropped = []
			#GameBoard.clearBoard(AI_grid)
			AI_grid = copy.deepcopy(grid)
			#moveOtherScore = minimax(move, otherPlayer)
			moveScore = minimax(move, player)
			#print("AI Score: ",moveScore)
			if moveScore == 300:
				#print("I have 3",move)
				return move+1
			#printGridAI()
			GameBoard.cancel(move+1,AI_grid)
			#GameBoard.cancel(move,AI_grid)
			moveOtherScore = minimax(move, otherPlayer)
			#print("MY Score: ",moveOtherScore)
			if moveOtherScore == 300:
				#print("Other have 3",move)
				return move+1
			#printGridAI()
			GameBoard.cancel(move+1,AI_grid)

			moveScore = minimax(move, player)
			scoreList.append(moveScore)
			#print("Depth 1,", dropped)
			#minimax(move, player)
			#if depth > 1:
			#	for d in range(0,depth):

			if depth > 1:
				for move1 in AI.possibleMovesAI():

					moveOtherScore = minimax(move, otherPlayer)
					#if moveOtherScore == 300:
					#	print("Other have 3",move)
					#	return move+1
					scoreList.append(-1*moveOtherScore)
					if depth > 2 and AI.canMove(move,AI_grid) == True:
						for move2 in AI.possibleMovesAI():
							scoreList.append(minimax(move2, player))
							if depth > 3 and AI.canMove(move2,AI_grid) == True:
								for move3 in AI.possibleMovesAI():
									scoreList.append(-1*minimax(move3, otherPlayer))
									if depth > 4 and AI.canMove(move3,AI_grid) == True:
										for move4 in AI.possibleMovesAI():
											scoreList.append(minimax(move4, player))
											if depth > 5 and AI.canMove(move4,AI_grid) == True:
												for move5 in AI.possibleMovesAI():
													scoreList.append(-1*minimax(move5, otherPlayer))
													if depth > 6 and AI.canMove(move5,AI_grid) == True:
														for move6 in AI.possibleMovesAI():
															scoreList.append(minimax(move6, player))
													elif AI.canMove(move5,AI_grid) == False:
														GameBoard.cancel(move5, AI_grid)
											elif AI.canMove(move4,AI_grid) == False:
												GameBoard.cancel(move4, AI_grid)
									elif AI.canMove(move3,AI_grid) == False:
										GameBoard.cancel(move3, AI_grid)
							elif AI.canMove(move2,AI_grid) == False:
								GameBoard.cancel(move2, AI_grid)
					elif AI.canMove(move1,AI_grid) == False:
						GameBoard.cancel(move1, AI_grid)
														#GameBoard.clearBoard(AI_grid)
														#AI_grid = copy.deepcopy(grid)
							#print("Depth 3,", dropped)
							#if depth > 3:
							#	print("Depth 3,", dropped)
							#	for move3 in AI.possibleMoves():
							#		scoreList.append(minimax(move3, otherPlayer))
							#		if depth > 4:
							#			print("Depth 4,", dropped)
							#			for move4 in AI.possibleMoves():
							#				scoreList.append(minimax(move4, player))
			#printGridAI()
			#a=input()
			score = 0
			for next in scoreList:
				score = score + next
			score = score/len(scoreList)
			#print("MOVE", move, "Score:", score)
			#aa=input("should: ")
			if score > bestScore:
				bestScore = score
				bestMove = move
			#print(dropped)
			#for clearNeed in dropped:
			#printGridAI()
			GameBoard.clearBoard(AI_grid)
		#		GameBoard.cancel(clearNeed,AI_grid)

		#		print("Canceled", clearNeed)
		#		print("GRID AI")
		#		printGridAI()
		#		print("GRID")
		#		printGrid()
		#		print("Canceled", clearNeed)
		#		aa=input()
			#dropped = []

		return bestMove+1
			
	def utility(check):
		
		if GameBoard.fourInRow(check,AI_grid) == True:
			utilityVal = 300
		elif GameBoard.threeInRow(check,AI_grid) == True:
			utilityVal = 200
		elif GameBoard.twoInRow(check,AI_grid) == True:
			utilityVal = 100
		else:
			utilityVal = 0
		return utilityVal
			
		
def printGrid():
	for y in range(0,len(grid)):
	#y=7-y
		print("|", end = '')
		for x in range(0,len(grid[y])):
			if grid[5-y][x] == 1:
				color = Fore.BLUE
			elif grid[5-y][x] == 2:
				color = Fore.RED
			else:
				color = Fore.WHITE
			print(color+str(grid[5-y][x])+Fore.WHITE+"|", end = '')
		print()
def printGridAI():
	for y in range(0,len(AI_grid)):
	#y=7-y
		print("|", end = '')
		for x in range(0,len(AI_grid[y])):
			print(str(AI_grid[5-y][x])+"|", end = '')
		print()

#myBoard = GameBoard(7,6)

#GameBoard.place(1,2)
#GameBoard.place(1,3)

#myBoard.place(3,7)



#AI_grid[3][3] = ' '


#print(grid)
#print(AI.canMove(3))
flag = True
while flag:
	for g in range(1,3):
		os.system("clear")
		printGrid()
		print(f"{Fore.GREEN} 1 2 3 4 5 6 7 {Fore.WHITE}")
		#print("Player 1: \n-------------")
		#print(GameBoard.fourInRow(1,grid))
		#print("Player 2: \n-------------")
		#print(GameBoard.fourInRow(2,grid))
		if GameBoard.fourInRow(1,grid) == True:
			break
		if GameBoard.fourInRow(2,grid) == True:
			break
		#print("Recommended Move: ",AI.nextMove(AI.possibleMoves(),g,False))
	#if GameBoard.winningMove(1,2)==True or GameBoard.winningMove(2,2)==True:
		#flag = False
		#k
		if g == 2:
			GameBoard.place(AI.nextMove(2, 7),2)
			#a = input()
		if g == 1:
			#GameBoard.place(AI.nextMove(1, 7),1)
			#a = input()
			try:
				inCol = int(input("Player "+" >>  "))
				GameBoard.place(inCol,1)
			except IndexError:
				print(f"{Fore.ORANGE}Sorry. You cannot place there.{Fore.WHITE}")
				time.sleep(2)
		os.system("clear")
		printGrid()

		#if GameBoard.winningMove(2,4) == True:
			#break
	if GameBoard.fourInRow(1,grid) == True:
		time.sleep(2)
		break
	if GameBoard.fourInRow(2,grid) == True:
		time.sleep(2)
		break
	#if GameBoard.winningMove(2,4) == True:
		#time.sleep(2)
		#break
	#myGameState 
	#os.system("clear")


if GameBoard.fourInRow(1,grid)==True:
	print("Congratulations! Player 1 Wins the Game")
elif GameBoard.fourInRow(2,grid)==True:
	print("Congratulations! Player 2 Wins the Game")
