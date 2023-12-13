class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def display(self):
        print(self.stack)
    def stacktoque(self):
        que=[]
        while self.stack:
            que.append(self.pop())
        que.reverse()
        return que
s=Stack()
s.push(8)
s.push(9)
s.push(10)
s.display() 
que=s.stacktoque()
print("que is",que)       