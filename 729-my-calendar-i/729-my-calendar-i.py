class MyCalendar:

    def __init__(self):
        self.interval = []

    def book(self, start: int, end: int) -> bool:
        if not self.interval:
            self.interval.append((start,end))
            return True
        else:
            index = bisect_right(self.interval,(start,end))
            if index == 0 and end <= self.interval[0][0]:
                self.interval = [(start,end)]+self.interval
                return True
            elif index == len(self.interval) and start >= self.interval[index-1][1]:
                self.interval.append((start,end))
                return True
            elif start >= self.interval[index-1][1] and end <= self.interval[index][0]:
                # current = self.interval[index]
                # prev = (start,end)
                # for i in range(index,len(self.interval)-1):
                #     self.interval[i] = self.interval[index]
                #     current = self.interval[i+1]
                # self.interval.append(current)
                self.interval.insert(index,(start,end))
                return True
            return False
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)