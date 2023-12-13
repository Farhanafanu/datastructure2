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
    def display(self):
        n=self.head
        while n:
            print(n.data)
            n=n.ref
def linkedtoque(l):
    que=[]
    n=l.head
    while n:
        que.append(n.data)
        n=n.ref
    return que
l=Linkedlist()
l.add(1)
l.add(2)
l.add(3)
l.display()
q=linkedtoque(l)
print(q)
        
        