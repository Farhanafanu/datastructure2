class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def hashfunction(self,key):
        return key %self.size
    def quadratic(self,key,i):
        c1=1
        c2=2
        return(self.hashfunction(key)+i*c1+c2(i**2))%self.size
    def insert(self,key,value):
        index=self.hashfunction(key)
        if self.table[index] is None:
            self.table[index]=(key,value)
        else:
            i=1
            while i<self.size:
                index=self.quadratic(key,i)
                if self.table[index] is None:
                    self.table[index]=(key,value)
                i+=1
    def display(self):
        for item in self.table:
            while item:
                print({item[0]:item[1]})
                break
            print("npne")


h=Hashtable(10)
h.insert(2,"apple")
h.insert(8,"orange")
h.display()
        