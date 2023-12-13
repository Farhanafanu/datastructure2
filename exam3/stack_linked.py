class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def stacktolinked(self):
        linkedlist=None
        while self.stack:
            data=self.pop()
            newnode=Node(data)
            newnode.ref=linkedlist
            linkedlist=newnode
        return linkedlist
    
s=Stack()
s.push(16)
s.push(18)
s.push(32)
linkedhead=s.stacktolinked()
n=linkedhead
while n:
    print(n.data)
    n=n.ref
