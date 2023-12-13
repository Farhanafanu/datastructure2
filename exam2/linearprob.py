class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def hashfunction(self,key):
        return key %self.size
    def insert(self,key,value):
        index=self.hashfunction(key)
        if self.table[index] is not None:
            index=(index+1)%self.size
        self.table[index]=(key,value)
    def search(self,key):
        index=self.hashfunction(key)
        current=self.table[index]
        while current:
            if self.table[index][0]==key:
                return self.table[index][1]
            index=(index+1)%self.size
    def remove(self,key):
        index=self.hashfunction(key)
        if self.table[index][0]==key:
            self.table[index]=None
        index=(index+1)%self.size
    def display(self):
        for item in self.table:
            while item:
                print({item[0]:item[1]})
                break
            print("none")
h=Hashtable(10)
h.insert(1,"banana")
h.insert(2,"orange")
print(h.search(2))
        