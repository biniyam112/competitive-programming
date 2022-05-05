class MyStack:
    nums = deque()
    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        return self.nums.pop()

    def top(self) -> int:
        if len(self.nums) > 0:
            return self.nums[-1]

    def empty(self) -> bool:
        return len(self.nums) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()