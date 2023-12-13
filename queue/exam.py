class Que:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        self.que.pop(0)
    def rear(self):
        print(self.que[-1])
    def front(self):
        print(self.que[0])
    def display(self):
        print(self.que)
q=Que()
q.enque(10)
q.enque(12)
q.enque(65)
q.rear()
q.front()
q.display()
        