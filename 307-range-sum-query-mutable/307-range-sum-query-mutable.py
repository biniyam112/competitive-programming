class NumArray:
    nums = []
    partSum = []
    length = 0
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = math.ceil(len(nums)/math.sqrt(len(nums)))
        self.partSum = [0] * self.length
        for i in range(len(nums)):
                self.partSum[i//self.length] += nums[i]

    def update(self, index: int, val: int) -> None:
        i = index//self.length
        self.partSum[i] += val-self.nums[index]
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        l = left//self.length
        r = right//self.length
        if r == l:
            for i in range(left,right+1):
                total += self.nums[i]
        else:
            for i in range(left,(l+1) * int(self.length)):
                total += self.nums[i]
            for i in range(l+1,r):
                total += self.partSum[i]
            for i in range(int(r * self.length),right+1):
                total += self.nums[i]
        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)