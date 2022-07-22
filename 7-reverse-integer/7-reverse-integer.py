class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        if x ==0:
            return 0
        sign = x/abs(x)
        x = abs(x)
        while x >= 10:
            digits.append(x%10)
            x//=10
        digits.append(x)
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10**(len(digits)-i-1)
        if num > (2 ** 31)-1 or num < -2 **31:
            return 0
        return int(sign * num)
        