class RandomizedSet:

    def __init__(self):
        self.container = {}
        self.removed = {}
        self.lista = []
        

    def insert(self, val: int) -> bool:
        output = False
        if val not in self.container:
            self.container[val] = 1
            self.lista.append(val)
            output = True
        elif val not in self.removed:
            return False
        elif self.container[val] == self.removed[val]:
            self.container[val] += 1
            output = True
        return output
        

    def remove(self, val: int) -> bool:
        output = False
        if val not in self.container:
            return False
        if val in self.container and (val not in self.removed or self.container[val] > self.removed[val]):
            output = True
            if val not in self.removed:
                self.removed[val] = 1
            else:
                self.removed[val] += 1
        return output
        

    def getRandom(self) -> int:
        while True:
            rand = random.randint(0,len(self.lista)-1)
            if self.lista[rand] not in self.removed:
                return self.lista[rand]
            elif self.container[self.lista[rand]] > self.removed[self.lista[rand]]:
                return self.lista[rand]
                
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()