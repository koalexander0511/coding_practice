#"Cracking the Coding Interview" 6th ed.
"""
Problem 8.4

Write a method to return all subsets of a set
"""

s = [0,1,2,3,4,5,6,7,8,9];

def listToString(lst):
	lst.sort();
	s = "";
	for i in lst:
		s += str(i);
	return s;

def powerSet(s):
	powerSet = {};
	return powerSetHelper(s, powerSet);

def powerSetHelper(s,powerSet):

	currSet = listToString(s);

	if(currSet in powerSet):
		return powerSet[currSet];

	powerSet[currSet] = [listToString(s)];

	if(len(s) == 1):
		return [listToString(s), ""];

	for i in s[:]:
		s.remove(i);
		newSets = powerSetHelper(s[:],powerSet);
		powerSet[currSet] += newSets;
		
		s.append(i);

	powerSet[currSet].sort();
	return list(dict.fromkeys(powerSet[currSet]));


print(powerSet(s));
print(len(powerSet(s)));