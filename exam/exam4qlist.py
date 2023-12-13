class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        n=self.head
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
def linkedtoque(l):
    que=[]
    n=l.head
    while n:
        que.append(n.data)
        n=n.ref
    return que
l=Linkedlist()
l.add(9) 
l.add(7)
l.add(6)
q=linkedtoque(l)
print(q)               