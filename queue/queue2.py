class Que:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        self.que.pop(0)
    def front(self):
        print(self.que[0])
    def rear(self):
        print(self.que[-1])
    def display(self):
        print(self.que)
q=Que()
q.enque(8)
q.enque(10)
q.enque(65)
q.display()
q.front()
q.rear()
q.deque()
q.display()
        