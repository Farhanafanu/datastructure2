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
    def display(self):
        print(self.stack)
    # def stacktoque(self):
    #     que=[]
    #     while self.stack:
    #         que.append(self.pop())
    #     return que
    def stacktolinked(self):
        linkedlist=None
        while self.stack:
            data=self.pop()
            newnode=Node(data)
            newnode.ref=linkedlist
            linkedlist=newnode
        return linkedlist
s=Stack()
s.push(10)
s.push(12)
s.push(13)
s.display()
# q=s.stacktoque()
# print("que",q)
linkedhead=s.stacktolinked()
n=linkedhead
while n:
    print(n.data)
    n=n.ref
        