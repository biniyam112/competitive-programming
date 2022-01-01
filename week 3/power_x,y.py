def myPow( x: float, n: int) -> float:
    def recursion(x : float,n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if n > 0:
            if n %2 == 0:
                return recursion(x,n/2) **2
            else:
                return x * recursion(x,(n-1)/2) ** 2
        else:
            if n%2 == 0:
                return recursion(x,n/2) ** 2
            else:
                return 1/x * recursion(x,(n+1)/2) ** 2
    print(recursion(x,n))
    return recursion(x,n)


myPow(2,-2)