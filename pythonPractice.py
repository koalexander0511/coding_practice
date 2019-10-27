def changeValue(x):
	print("\t->immutable")
	x  = 100

def changeList(l):
	print("\t->mutable")
	print("\t->indexable")
	l[0] = -1

def changeDict(d):
	print("\t->mutable")
	print("\t->indexable")
	d[1] = "ONE"
	d[-1] = "NEW!"
	d[7].append(0);

def changeTuple(t):
	print("\t->immutable")
	print("\t->indexable")
	#t[0] = '1'; #error! tuple object is immutable
	index = t[0]

def changeStr(s):
	print("\t->immutable")
	print("\t->indexable")
	#s[0] = '1'; #error! string object is immutable
	index = s[0]

def changeSet(s):
	print("\t->immutable")
	print("\t->unindexable")
	if 1 in s:
		s.remove(1)
	s.add(1000)


x = 10
print("\nINTEGER")
print("Before:", x)
changeValue(x)
print("After: ",x)

l = [1, 2, 3, 4, 5, 6]
print("\nLIST")
print("Before:", l)
changeList(l)
print("After: ",l)

d = {1:"one",2:"two",7:[0,1,1,1]}
print("\nDICTIONARY")
print("Before:", d)
changeDict(d)
print("After: ",d)

strn = "Hello World!"
print("\nSTRING")
print("Before:", strn)
changeStr(strn)
print("After: ",strn)

tpl = (1 ,2 ,3 ,4 ,5,6,7)
print("\nTUPLES")
print("Before:", tpl)
changeTuple(tpl)
print("After: ",tpl)

s = {7,1 ,2 ,3 ,4 ,5 ,6 }
print("\nSETS")
print("Before:", s)
changeSet(s)
print("After: ",s)