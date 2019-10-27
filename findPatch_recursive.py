import random


DEBUGMODE = False


"""
Resursive solution for finding largest patch
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
				if(random.randrange(0,freq) > 0):
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

def fillMaxGrid(matrix, maxGrid, r, c):
	#increase recursion limit so the program doesn't exit out
	import sys
	sys.setrecursionlimit(3000)

	#base case
	#the edges can only have a patch equal to the value in matrix[r][c]
	if(r == 0 or c == 0):
		maxGrid[r][c] = matrix[r][c]
		return matrix[r][c]

	#memoization
	#if we already computed maxGrid[r][c], use that instead of recursing again
	if(maxGrid[r][c] != float('inf')):
		return maxGrid[r][c]

	#the size of the patch for maxGrid[r][c] depends of its neighbors
	neighborMaxSqSize = min(
		fillMaxGrid(matrix,maxGrid,r-1,c),
		fillMaxGrid(matrix,maxGrid,r,c-1),
		fillMaxGrid(matrix,maxGrid,r-1,c-1)
		)

	#if the point (r,c) is white, take the minimum of its neighbors' patch size, and add one
	if(matrix[r][c] == 1):
		maxGrid[r][c] = 1 + neighborMaxSqSize
	#if the point (r,c) is not white, then we cannot make a patch
	else:
		maxGrid[r][c] = 0

	return maxGrid[r][c]

def findMaxPatch(matrix):
	#maxGrid:
	#size: same as matrix
	#for each element maxGrid[r][c], it stores the size of the patch, where
	#the bottom right point of that patch is (r,c)
	maxGrid = [float('inf')] * len(matrix)
	for i in range(0, len(matrix)):
		maxGrid[i] = [float('inf')] * len(matrix[0])

	fillMaxGrid(matrix, maxGrid, len(matrix)-1,len(matrix[0])-1)

	#after maxGrid is completed, find the largest number(=largest white patch) in it
	return max([max(i) for i in maxGrid])

#main
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