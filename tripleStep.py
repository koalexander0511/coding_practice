#"Cracking the Coding Interview" 6th ed.
"""
Problem 8.1

A child is running up a staircase with n steps and can hop 1, 2, or 3 steps at a time
Implement a method to count how many possible ways the child can run up the stairs
"""

import time;

n = int(input("Enter number of steps:"));

#Dynamic programming approach
def tripleStepDP(n):
	#mem stores the number of ways to reach the ith step
	mem = [0] * (n+1);
	mem[1] = 1;
	mem[2] = 2;
	mem[3] = 4;
	
	return tripleStepDPHelper(n, mem);

def tripleStepDPHelper(n, mem):
	if(mem[n] == 0):
		mem[n] = tripleStepDPHelper(n-1, mem) + tripleStepDPHelper(n-2, mem) + tripleStepDPHelper(n-3, mem);
	
	return mem[n];

#Recursive approach
def tripleStepRecur(n):
	if(n == 1):
		return 1;
	elif(n == 2):
		return 2;
	elif(n == 3):
		return 4;
	else:
		return tripleStepRecur(n-1) + tripleStepRecur(n-2) + tripleStepRecur(n-3);
start_time = time.time();
print("# of ways to climb up", n, "stairs:", tripleStepDP(n));
total_time = time.time() - start_time;
print("Execution time (DP Approach):", total_time);

#not going to go through the computation if n > 30; takes too long
if(n < 30):
	start_time = time.time();
	tripleStepRecur(n);
	total_time_recur = time.time() - start_time;
else:
	total_time_recur = "long!"

print("Execution time (Recursive Approach):", total_time_recur);
