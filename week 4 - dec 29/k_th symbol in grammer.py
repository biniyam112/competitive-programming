    def kthGrammar( n: int, k: int) -> int:
        # def recursion(n):
        #     if n ==  1:
        #         return '0'
        #     s = ''
        #     for i in recursion(n-1):
        #         if i =='0':
        #             s+='01'
        #         else :
        #             s+='10'
        #     return s
        # return recursion(n)[k-1]
        def recursion(n,key):
            if n ==1:
                return '0'
            if key % 2 == 0:
                value = recursion(n-1,key/2)
                if value == '0' :
                    return '1'
                else:
                    return '0'
            else:
                value = recursion(n-1,(key+1)/2)
                if value == '0':
                    return '0'
                else:
                    return '1'
        return recursion(n,k)
    
    
kthGrammar(20,100)