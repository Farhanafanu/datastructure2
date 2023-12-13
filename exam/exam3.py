class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

        
class QUe:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        return self.que.pop(0)
    def display(self):
        print(self.que)
    # def quetostack(self):
    #     stack=[]
    #     while self.que:
    #         stack.append(self.deque())
    #     return stack
    def quetolinked(self):
        linkedlist=None
        while self.que:
            data=self.deque()
            newnode=Node(data)
            newnode.ref=linkedlist
            linkedlist=newnode
        return linkedlist
q=QUe()
q.enque(8)
q.enque(9)
q.enque(10)
q.display()
# s=q.quetostack()
# print("stack is",s)
linkedhead=q.quetolinked()
n=linkedhead
while n:
    print(n.data)
    n=n.ref