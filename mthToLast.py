#Hackerrank problem

"""
M-th to last element

For this question, you will write a program that, 
given a positive integer M and a list of integers L, outputs the list element M links away from the end of the list. 
For this program, we will use 1-indexing. 
That means mth_to_last(1) is the "1st-to-last" element, or simply the last element in the list.
"""

class Node:
	def __init__(self, value):
		self.prev = None;
		self.next = None;
		self.value = value;

class LinkedList:
    def __init__(self):
    	self.curr = Node(None);
    	self.head = self.curr;
    	self.tail = self.curr;
    def add(self, value):
    	if(self.curr.value == None):
    		self.curr.value = value;
    	else:
	    	self.curr.next = Node(value);
    		self.curr.next.prev = self.curr;
    		self.curr = self.curr.next;
    		self.tail = self.curr;
    def getVal(self):
    	if(self.curr == None):
    		return None;
    	return self.curr.value;
    def next(self):
    	if(self.curr != None):
    		self.curr = self.curr.next;
    def prev(self):
    	if(self.curr != None):
    		self.curr = self.curr.prev;
    def setHead(self):
    	self.curr = self.head;
    def setTail(self):
    	self.curr = self.tail;

        
    
nth = int(input());
lst = [int(i) for i in input().strip().split(" ")];

ll = LinkedList();

print(lst);

for i in lst:
	ll.add(i);


ll.setTail();
for i in range(0,nth-1):
	ll.prev();

print(ll.getVal());