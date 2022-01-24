def countGoodNumbers( n: int) -> int:
    def recursion(n):
            if n == 1:
                return 5
            if n == 2:
                return 20
            if n % 2 == 0:
                if n/2 %2 ==0:
                    return  (recursion(n/2) **2) % ((10**9) + 7)        
                else:
                    return 20 * recursion(n-2) % ((10**9) + 7)
            else:
                if (n-1)/2%2 ==0:
                    return (5* recursion((n-1)/2) **2) % ((10**9) + 7)        
                else:
                    return 5 * recursion(n-1) % ((10**9) + 7)
    return recursion(n)                                                                          
        

countGoodNumbers(1000)