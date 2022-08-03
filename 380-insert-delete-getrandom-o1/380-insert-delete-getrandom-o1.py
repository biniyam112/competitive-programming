class RandomizedSet:

    def __init__(self):
        self.freq = {}
        self.ets = []
        

    def insert(self, val: int) -> bool:
        if val not in self.freq or self.freq[val] == 0:
            self.freq[val] = 1
            self.ets.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.freq or self.freq[val] == 0:
            return False
        self.freq[val] -= 1
        return True
        

    def getRandom(self) -> int:
        while True:
            rand = random.randint(0,len(self.ets)-1)
            if self.freq[self.ets[rand]] == 1:
                return self.ets[rand]
                
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()