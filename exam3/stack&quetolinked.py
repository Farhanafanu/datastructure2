# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if  self.stack is not None: 
#             return self.stack.pop()
#     def stacktolinked(self):
        
#         linkedlist=None
#         while self.stack:
#             data=self.pop()
#             newnode=Node(data)
#             newnode.ref=linkedlist
#             linkedlist=newnode
#         return linkedlist
# stack=Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# linnekdhead=stack.stacktolinked()
# n=linnekdhead
# while n:
#     print(n.data)
#     n=n.ref
        
#que to linked
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
    def quetolinked(self):
        linkedlist=None
        while self.que:
            data=self.deque()
            nenwode=Node(data)
            nenwode.ref=linkedlist
            linkedlist=nenwode
        return linkedlist
q=Que()
q.enque(10)
q.enque(87)
q.enque(52)
linkedhead=q.quetolinked()
n=linkedhead
while n:
    print(n.data)
    n=n.ref

        
        