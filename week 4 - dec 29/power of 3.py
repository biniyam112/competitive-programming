    def isPowerOfThree(n: int) -> bool:
        def recursion(n):
            if n == 0:
                return False
            if n == 1:
                return True
            if n % 3 == 0:
                return recursion(n//3)
            else:
                return False
        return recursion(n)
    
isPowerOfThree(12)