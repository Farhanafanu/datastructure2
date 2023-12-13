class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Que:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        return self.que.pop(0)
    def quetolinkedlist(self):
        linkedlist=None
        while self.que:
            data=self.deque()
            newnode=Node(data)
            newnode.ref=linkedlist
            linkedlist=newnode
        return linkedlist
    
q=Que()
q.enque(87)
q.enque(65)
q.enque(32)
linkeadhead=q.quetolinkedlist()
n=linkeadhead
while n:
    print(n.data)
    n=n.ref
