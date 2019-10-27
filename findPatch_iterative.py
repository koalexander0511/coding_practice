import random


DEBUGMODE = False

"""
Iterative solution for finding largest patch
Runtime: O(n*m), for a matrix of size n x m
Memory: O(n*m)
"""


#used during debugging for easy matrix creation
def createMatrix(n,m, freq = 2, randPatch = 0):
	matrix = [0] * n
	for i in range(0,n):
		matrix[i] = [0] * m

	if(randPatch):
		random.seed()
		for i in range(0,n):
			for j in range(0,m):
				if(random.randrange(0,10) > 0):
					matrix[i][j] = 1
				else:
					matrix[i][j] = 0

	return matrix

#used during debugging to print formatted matrices
def printMatrix(matrix):
	for row in matrix:
		for i in row:
			if(i):
				print(i, end=" ")
			else:
				print(" ", end=" ")
		print("")


def fillMaxGrid(matrix, maxGrid):
	maxGrid[0] = matrix[0]
	for i in range(0,len(matrix)):
		maxGrid[i][0] = matrix[i][0]

	for i in range(1,len(maxGrid)):
		for j in range(1,len(maxGrid[0])):
			if(matrix[i][j] == 1):
				maxGrid[i][j] = 1 + min(maxGrid[i-1][j], maxGrid[i][j-1], maxGrid[i-1][j-1])
			else:
				maxGrid[i][j] = 0

def findMaxPatch(matrix):
	#maxGrid:
	#size: same as matrix
	#for each element maxGrid[r][c], it stores the size of the patch, where
	#the bottom right point of that patch is (r,c)
	maxGrid = [float('inf')] * len(matrix)
	for i in range(0, len(matrix)):
		maxGrid[i] = [float('inf')] * len(matrix[0])

	fillMaxGrid(matrix, maxGrid)

	#after maxGrid is completed, find the largest number(=largest white patch) in it
	return max([max(i) for i in maxGrid])

def main():
	"""
	input
	1: number of rows
	2: number of columns
	3+: the values of the matrix, where each line represents one row
	
	example:
	3
	4
	0 0 0 0
	0 0 1 1
	0 0 1 1
	"""
	
	n = int(input())
	m = int(input())

	if(DEBUGMODE):
		matrix = createMatrix(n,m,2,1)
	else:
		matrix = [0] * n

		for i in range(0,n):
			matrix[i] = [int(i) for i in input().strip().split(" ")]

	return findMaxPatch(matrix)

if __name__  == "__main__":
	print(main())