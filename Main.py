import random

#finds sum of all indexs in board
def findSum(board):
	sum = 0;
	for row in board:
		for col in row:
			sum += col;
	return sum

#prints board
def print2DArray(board):
	for row in board:
		for col in row:
			print(col, "", end = "")
		print()	


#board
board = []

#fills board
for i in range(10):
	row = []
	for j in range(10):
		row.append(random.randint(0, 9))
	board.append(row)
print2DArray(board)
print(findSum(board))
