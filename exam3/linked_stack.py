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
def linkedtostack(l):
    stack=[]
    n=l.head
    while n:
        stack.append(n.data)
        n=n.ref
    return stack


l=Linkedlist()
l.add(10)
l.add(80)
l.add(76)
s=linkedtostack(l)
print("stack is",s)
