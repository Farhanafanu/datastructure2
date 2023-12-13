class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.ref=None
class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def hashfunction(self,key):
        return key %self.size
    def insert(self,key,value):
        index=self.hashfunction(key)
        newnode=Node(key,value)
        if self.table[index] is None:
            self.table[index]=newnode
        else:
            current=self.table[index]
            while current.ref:
                current-=current.ref
            current.ref=newnode
    def search(self,key):
        index=self.hashfunction(key)
        current=self.table[index]
        if current.key==key:
            return current.value
        return None
    def remove(self,key):
        index=self.hashfunction(key)
        current=self.table[index]
        prev=None
        while current:
            if prev is None:
                self.table[index]=current.ref
            else:
                prev.ref=current.ref
            break
        prev=current
        current=current.ref
    def display(self):
        for node in self.table:
            while node is not None:
                print({node.key:node.value})
                node=node.ref
            print("none")
h=Hashtable(10)
h.insert(1,"apple")
h.insert(2,"banaa")
# print(h.search(2))
h.remove(2)
h.display()        
        