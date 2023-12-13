class Que:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        return self.que.pop()
    def display(self):
        print(self.que)
    def quetostack(self):
        stack=[]
        while self.que:
            stack.append(self.deque())
        return stack
q=Que()
q.enque(10)
q.enque(70)
q.enque(86)
q.display()
s=q.quetostack()
print("stack is",s)
        