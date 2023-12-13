#linked to stack
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        newnode=Node(data)
        n=self.head
        if self.head is None:
            self.head=newnode
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def display(self):
        n=self.head
        if n is None:
            print("empty")
        else:
            while n is not None:
                print(n.data)
                n=n.ref
    def pop(self):
        n=self.head
        if n is None:
            print("empty")
        elif self.head.ref is None:
            self.head=None
        else:
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
def Linkedtostack(l):
    stack=[]
    n=l.head
    while n:
        stack.append(n.data)
        n=n.ref
    return stack
l=Linkedlist()
l.add(8)
l.add(19)
l.add(76)
l.display()
l.pop()
stack=Linkedtostack(l)
print(stack)
        
        