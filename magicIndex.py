#"Cracking the Coding Interview" 6th ed.
"""
Problem 8.3

A magic index in an array A[0...n-1] is when A[i] = i.
Given sorted array, find magic index.
"""

import random;

def magicIndex(arr):
	return magicIndexHelper(arr, 0, len(arr)-1);

def magicIndexHelper(arr, start, end):
	size = len(arr);
	mid = start + int((end-start)/2);

	if(start == end):
		if(start == arr[start]):
			return start;
		else:
			return -1;

	if(arr[mid] == mid):
		return mid;
	if(arr[mid] > mid):
		print("left");
		return magicIndexHelper(arr, start, mid);
	elif(arr[mid] < mid):
		print("right");
		return magicIndexHelper(arr, mid+1, end);

random.seed();

arrLen = 10000;
arr = [];

for i in range(0,arrLen):

	num = int(random.randrange(-arrLen/2,arrLen));
	while(num in arr):
		num = int(random.randrange(-arrLen,arrLen*2));
	arr += [num];


arr.sort();
print(arr);
print(magicIndex(arr));