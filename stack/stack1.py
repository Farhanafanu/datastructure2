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
s.push(9)
s.push(8)
s.push(15)
s.display()
s.top()
s.pop()
s.display()
#time O(1)
#space O(n)