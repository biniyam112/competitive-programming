class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n = str(bin(n))
        if n[-1] == 1:
            return False
        counter = 0
        for i in range(2,len(n)):
            if n[i] == '1':
                counter+=1
                if counter > 1:
                    return False
        return True
        
        
            