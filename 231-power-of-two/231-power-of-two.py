class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n = str(bin(n)[2:])
        if n[-1] == 1:
            return False
        counter = 0
        for i in n:
            if i == '1':
                counter+=1
                if counter > 1:
                    return False
        if counter == 0:
            return False
        return True
        
        
            