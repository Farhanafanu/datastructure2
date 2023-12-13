#que to stack
class Que:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        return self.que.pop(0)
    def quetostack(self):
        stack=[]
        while self.que:
            stack.append(self.deque())
        return stack
q=Que()
q.enque(8)
q.enque(1)
q.enque(2)
s=q.quetostack()
print("stack is",s)
        