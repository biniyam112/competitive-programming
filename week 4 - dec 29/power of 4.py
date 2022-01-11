    def isPowerOfFour( n: int) -> bool:
        def recursion(n):
            if n == 0:
                return False
            if n == 1:
                return True
            if n %4 == 0:
                return recursion(n//4)
            else:
                return False
        return recursion(n)
    


isPowerOfFour(32)