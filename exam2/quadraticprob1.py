class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size

    def hashfunction(self,key):
        return key %self.size
    def quadratic(self,key,i):
        c1=1
        c2=2
        return (self.hashfunction(key)+c1*i+c2(i**2))%self.size
    def insert(self,key,value):
        index=self.hashfunction(key)
        if self.table[index] is None:
            self.table[index]=(key,value)
        else:
            i=1
            if i<self.size:
                index=self.quadratic(key,i)
                if self.table[index] is None:
                    self.table[index]=(key,value) 
                i+=1
    def search(self,key):
        index=self.hashfunction(key)
        if self.table[index] is not None and self.table[index][0]==key:
            return self.table[index][1]
        else:
            i=1
            if i<self.size:
                index=self.quadratic(key,i)
                if self.table[index][0]==key:
                    return self.table[index][1] 
                i+=1
h=Hashtable(10)
h.insert(2,"apple")
h.insert(8,"orange")
print(h.search(2))   