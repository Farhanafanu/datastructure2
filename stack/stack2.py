class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_Empty():
            self.stack.pop()
        else:
            print("stack is empty")
    def is_Empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def top(self):
        if not self.is_Empty():
            return self.stack[-1]
        else:
            print("empty")
    def printstack(self):
        if not self.is_Empty():
            print(self.stack)
        else:
            print("empty")
s=Stack()
s.push(10)
s.push(80)
s.push(70)
s.pop()
s.printstack()
        