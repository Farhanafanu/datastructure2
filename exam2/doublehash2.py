class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    def hashfunction1(self,key):
        return key %self.size
    def hashfunction2(self,key):
        return 7 -(key %7)
    def insert(self,key,value):
        index=self.hashfunction1(key)
        if self.table[index] is None:
            self.table[index]=(key,value)
        else:
            index2=index
            i=1
            while True:
                index2=(index+i*self.hashfunction2(key))%self.size
                if self.table[index2] is None:
                    self.table[index2]=(key,value)
                i+=1
                if i == self.size:  # Avoid infinite loop
                    break
    def search(self,key):
        index=self.hashfunction1(key)
        if self.table[index] is not None and self.table[index][0]==key:
            return self.table[index][1]
        else:
            i=1
            index2=index
            index2=(index+i*self.hashfunction2(key))%self.size
            if self.table[index2] is not None and self.table[index2][0]==key:
                return self.table[index2][1]
            i+=1
            
h=Hashtable(7)
h.insert(1,"apple")
h.insert(1,"banana")
print(h.search(1))



        