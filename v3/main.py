import random
import time
import os
from copy import deepcopy
from colorama import Fore
import numpy as np

turn = 1

gameBoard = [[0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0]]
					  
def canMove(board,column):
	return False if board[5][column-1] != 0 else True
def place(board,column,player):
	for i in range(len(board)):
		if board[i][column] == 0:
			board[i][column] = player
			break
	return board
def cancel(board,column):
	for i in range(len(board)):
		if board[i][column] == 0 and i != 0:
			board[i-1][column] = 0
			break
	return board
def clearBoard(board):
	for iy in range(len(board)):
		for ix in range(len(board[iy])):
			board[iy][ix] = 0
	return board
def countInRow(board,player):
	countList = [0,0,0,0,0,0,0]
	blockList = set()
	def countLoop(r_board,tempx,tempy,direction,r_player):
		posList = []
		count=0
		while tempx < len(r_board[iy]) and tempy < len(r_board) and tempx >= 0 and tempy >= 0 and r_board[tempy][tempx] == r_player:
			count+=1
			posList.append(str(tempx)+','+str(tempy))
			if direction == 0:
				tempx+=1
			elif direction == 1:
				tempy+=1
			elif direction == 2:
				tempx-=1
				tempy+=1
			else:
				tempx+=1
				tempy+=1
		#print(posList)
		return count,posList
	for iy in range(0,len(board)):
		for ix in range(0,len(board[iy])):
				for i in range(0,3):
					index,newBlock = countLoop(board,ix,iy,i,player)
					blockList.update(newBlock)
	#print(blockList)
	for x in blockList:
		ix = int(x.split(',')[0])
		iy = int(x.split(',')[1])
		for i in range(0,4):
			#print("called function",ix,iy)
			index,newBlock = countLoop(board,ix,iy,i,player)
			#print("returned",index)
			countList[index]+=1
		#print(countList)
	return countList
def printBoard(board):
	for y in range(0,len(board)):
	#y=7-y
		print("|", end = '')
		for x in range(0,len(board[y])):
			if board[5-y][x] == 1:
				color = Fore.BLUE
			elif board[5-y][x] == 2:
				color = Fore.RED
			else:
				color = Fore.WHITE
			print(color+str(board[5-y][x])+Fore.WHITE+"|", end = '')
		print()
def fourInRow(board,player):
	return countInRow(board,player)[4]>0

class AI:
	def __init__(self,depth):
		self.depth = depth
	def possibleMoves(self,board,player):
		posMoveList = []
		for i in range(0,7):
			if canMove(board,i) == True:
				posMoveList.append([i,place(deepcopy(board),i,player)])
		return posMoveList
	def getMoveWithUtility(self,board,player,util):
		moves = self.possibleMoves(board,player)
		for i in moves:
			#print("self.diff_utility(i[1],player)",self.diff_utility(i[1],player))
			if self.diff_utility(i[1],player) == util:
				return i[0]
	def utility(self,board,player):
		util_list = countInRow(board,player)
		utilityVal = 0
		if util_list[4] > 0:
			return 100000
		for i in range(len(util_list)):
			utilityVal += util_list[i]*i
		return utilityVal
	def diff_utility(self,board,player):
		if player == 1:
			return self.utility(board,1) - self.utility(board,2)
		elif player == 2:
			return self.utility(board,2) - self.utility(board,1)
	def makeMove(self,board):
		set_depth = self.depth
		global v_list_col, v_list_val
		v_list_col = []
		v_list_val = []
		def max_value(state,set_depth):
			global v_list_col, v_list_val
			#printBoard(state)
			#print("depth",set_depth)
			set_depth-=1
			if abs(self.diff_utility(state,2)) > 10000 or set_depth < 1:
			#	print("max return self.diff_utility(state,2)",self.diff_utility(state,2))
				return self.diff_utility(state,2)
			v = -np.inf
			v_list_col = []
			v_list_val = []
			for i in self.possibleMoves(state,2):
				#print("Max move col",i[0])
				v_list_val.append(min_value(i[1],set_depth))
				if set_depth < 1:
					v_list_col.append(i[0])
					v = max(v_list_val)
					#print("Return",v_list_col[v_list_val.index(v)])
					#print("v_list_col",v_list_col)
					return v_list_col[v_list_val.index(v)]
			v = max(v_list_val)
			#print("max returned", v)
			return v
		def min_value(state,set_depth):
			#printBoard(state)
			#print("depth",set_depth)
			set_depth-=1
			if abs(self.diff_utility(state,2)) > 10000 or set_depth < 1:
			#	print("min return self.diff_utility(state,2)",self.diff_utility(state,2))
				return self.diff_utility(state,2)
			v = np.inf
			for i in self.possibleMoves(state,1):
				#print("Min move col",i[0])
				v = min(v, max_value(i[1],set_depth))
			#print("min returned", v)
			return v
		v = max_value(board,set_depth)
		#print("v:",v)
		return v #self.getMoveWithUtility(board,2,v)
			
opponentAI = AI(2)

#GameBoard.place(1,2)
#GameBoard.place(1,3)

#myBoard.place(3,7)



#AI_grid[3][3] = ' '


#print(grid)
#print(AI.canMove(3))
moveResult = 0
while True:
	for g in range(1,3):
		os.system("clear")
		printBoard(gameBoard)
		#print("moveResult",moveResult+1)
		print(f"{Fore.GREEN} 1 2 3 4 5 6 7 {Fore.WHITE}")
		if fourInRow(gameBoard,1)==True:
			print("Congratulations! Player 1 Wins the Game")
			exit()
		if fourInRow(gameBoard,2)==True:
			print("Congratulations! Player 2 Wins the Game")
			exit()
		if g == 2:
		#	GameBoard.place(AI.nextMove(2, 7),2)
			moveResult = opponentAI.makeMove(gameBoard)
			print("moveResult",moveResult)
			#a=input()
			place(gameBoard,moveResult,2)
		if g == 1:
			#GameBoard.place(AI.nextMove(1, 7),1)
			#a = input()
			try:
				inCol = int(input("Player "+" >>  "))
				place(gameBoard,inCol-1,1)
			except IndexError:
				print(f"{Fore.ORANGE}Sorry. You cannot place there.{Fore.WHITE}")
				time.sleep(2)

		#if GameBoard.winningMove(2,4) == True:
			#break
	#if GameBoard.winningMove(2,4) == True:
		#time.sleep(2)
		#break
	#myGameState 
	#os.system("clear")



