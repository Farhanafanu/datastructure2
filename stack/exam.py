class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    def top(self):
        print(self.stack[-1])
    def display(self):
        print(self.stack)
s=Stack()
s.push(8)
s.push(10)
s.push(12)
s.top()
s.display()
s.pop()
s.display()
        