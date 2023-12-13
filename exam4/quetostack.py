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
q.enque(9)
q.enque(10)
q.enque(11)
stack=q.quetostack()
print("stack is",stack)