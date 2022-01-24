    def findKthBit( n: int, k: int) -> str:
        def invert(value):
            s = ''
            for i in range(len(value)-1,-1,-1):
                if value[i] == '0':
                    s+='1'
                else:
                    s+='0'
            return s
        def recursion(n):
            if n == 1:
                return "0"
            else:
                s = recursion(n-1)
                return s + "1" + ''.join(invert(s))
        return recursion(n)[k-1]
    
findKthBit(4,11)