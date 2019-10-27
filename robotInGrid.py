#"Cracking the Coding Interview" 6th ed.
"""
Problem 8.2

Robot sitting on the top left corner of a r x c grid.
Robot can only move right or down.
Certain cells are "off limits"; cannot step on them
Design an algorithm to find a path from top left to bottom right
"""

#r = 5;
#c = 5;
#grid = [[1] * r] * c;

import random;

class Grid:
	def __init__(self, grid):
		self.grid = grid;
		self.numRows = len(self.grid);
		self.numCols = len(self.grid[0]);


def robotInGrid(g):
	return robotInGridHelper(g, 0, 0, [[]]);

def robotInGridHelper(g, r, c, path):
	if(g.grid[r][c] == 0):
		return [];
	if(r == g.numRows-1 and c == g.numCols-1):
		return path + [[r,c]];

	if(r < g.numRows-1):
		path1 = robotInGridHelper(g, r+1,c, path);
		if(len(path1) != 0):
			return path1 + [[r,c]];


	if(c < g.numCols-1):
		path2 = robotInGridHelper(g, r,c+1, path);
		if(len(path2) != 0):
			return path2 + [[r,c]];

	g.grid[r][c] = 0;
	return [];

rowSize = int(input("Enter row size:"));
colSize = int(input("Enter column size:"));

"""
grid = [
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1],
		[1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1]
	]
"""

grid = [1] * colSize;
for i in range(0,rowSize):
	grid[i] = [1] * rowSize;
memGrid = [1] * colSize;
for i in range(0,rowSize):
	memGrid[i] = [1] * rowSize;

random.seed();
frequency = 0.3;



for i in range(0, int((rowSize*colSize)*frequency)):
	random.seed();
	c = int(random.random()*rowSize);
	r = int(random.random()*colSize);
	grid[r][c] = 0;
	memGrid[r][c] = 0;

grid[0][0] = 1;
memGrid[0][0] = 1;

g = Grid(memGrid);


print("Original Maze:");
print(" " + "_ " * len(grid[0]));
for i in range(0,len(grid)):
	print("|", end="");
	for j in range(0,len(grid[0])):
		if(grid[i][j] == 1):
			print("_|", end = "");
		else:
			print(":|", end = "");
	print("");

path = robotInGrid(g);

print("\nSolved:");
print(" " + "_ " * len(grid[0]));
for i in range(0,len(grid)):
	print("|", end="");
	for j in range(0,len(grid[0])):
		if([i, j] in path):
			print("O|", end = "");
		elif(grid[i][j] == 1):
			print("_|", end = "");
		else:
			print(":|", end = "");
	print("");

if(len(path) == 0):
	print("No path available!");