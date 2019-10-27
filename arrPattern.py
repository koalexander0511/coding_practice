lst = input("Enter list of characters:")
pattern = [lst[0]];
matchIndex = 0;
repCount = 0;

for i in range(1,len(lst)):
	print("lst:\t", lst);
	print("i:",i,"\t", " "*(i-1), "^");
	print("pattern:", pattern);
	print("matchIndex:", matchIndex);
	print("repCount:", repCount);
	
	#The lst is following the pattern
	if(lst[i] == pattern[matchIndex]):
		matchIndex += 1;
		if(matchIndex == len(pattern)):
			matchIndex = 0;
			repCount += 1;

		print("The list is following the pattern");

	#the lst is not following the pattern
	else:
		matchIndex = 0;
		pattern = lst[0:i+1];
		repCount = 0;
		print("The list is not following the pattern");

	print("");


if(repCount > 0):
	print("Pattern is:", pattern);
else:
	print("No pattern found!");
