class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        for i in range(len(strs)):
            zeros = 0
            ones = 0
            for j in strs[i]:
                if j == '0':
                    zeros+=1
                else:
                    ones+=1
            strs[i] = [ones+zeros,zeros,ones,strs[i]]
        index = 0
        @cache
        def dp(m,n,index):
            if m < 0 or n < 0:
                return -math.inf
            if index == len(strs):
                return 0
            return max(dp(m,n,index+1),1+dp(m-strs[index][1],n-strs[index][2],index+1))
        return dp(m,n,index)
            
            
            
            
        