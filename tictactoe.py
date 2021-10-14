"""This is a basic TIC TAC TOE (X or O) game which, I've made using pyhton"""
square = ['0','1','2','3','4','5','6','7','8','9']
def invalid(num):
	if num > 0 and num <=9: 
		return False
	else:
		return True
def checkWin():
	if (square[1]==square[4] and square[4]==square[7]):
		return '1'
	if (square[2]==square[5] and square[5]==square[8]):
		return '1'
	if (square[3]==square[6] and square[6]==square[9]):
		return '1';
	if (square[1]==square[2] and square[2]==square[3]):
		return '1'
	if (square[4]==square[5] and square[5]==square[6]):
		return '1'
	if (square[7]==square[8] and square[8]==square[9]):
		return '1'
	if (square[7]==square[8] and square[8]==square[9]):
		return '1'
	if (square[1]==square[5] and square[5]==square[9]):
		return '1'
	if (square[3]==square[5] and square[5]==square[7]):
		return '1'
def drawBoard():
	print("Made By:- Harsh Verma.")
	print("\n\n\t\t\t\t\t\t T i c  T a c  T o e  G a m e\n\n\t\t\t",sep="", end="")
	print("\t\t\t*****************************",sep="", end="")
	print("\n\n\t\t\t\t\t\tPLAYER 1 (X)  --  PLAYER 2 (O) \n\n\n",sep="", end="")
	print("\t\t\t\t\t\t......................\n",sep="", end="")
	print("\t\t\t\t\t\t|      |      |      |\n",sep="", end="")
	print("\t\t\t\t\t\t|  ",square[1],"   |   ",square[2],"  |   ",square[3],"  |\n",sep="", end="")
	print("\t\t\t\t\t\t|......|......|......|\n",sep="", end="")
	print("\t\t\t\t\t\t|      |      |      |\n",sep="", end="")
	print("\t\t\t\t\t\t|  ",square[4],"   |   ",square[5],"  |   ",square[6],"  |\n",sep="", end="")
	print("\t\t\t\t\t\t|......|......|......|\n",sep="", end="")
	print("\t\t\t\t\t\t|      |      |      |\n",sep="", end="")
	print("\t\t\t\t\t\t|  ",square[7],"   |   ",square[8],"  |   ",square[9],"  |\n",sep="", end="")
	print("\t\t\t\t\t\t|......|......|......|\n",sep="", end="")
	print("\t\t\t\t\t\t                      \n",sep="", end="")
	
if __name__ == '__main__':
	chances = []
	player=int(1)
	drawBoard()
	while (not checkWin()):
		player+=1
		print("PLAYER",(player%2)+1,": ", sep=" ", end="")
		chance = int(input())
		if invalid(chance) or chance in chances:
			print("INVALID INPUT")
			exit();
		if player%2==0:
			square[chance] = 'X'
		else:
			square[chance] = 'O'
		drawBoard()
		chances.append(chance)
		if checkWin() == '1':
			if player%2==0:
				print("PLAYER 1 WON!!")
			else:
				print("PLAYER 2 WON!!")
	else:
		print("GAME OVER!!")
