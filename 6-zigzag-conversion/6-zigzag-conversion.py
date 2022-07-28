class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows:
            return s
        split = []
        i = 0
        while i < len(s):
            j = 0
            temp = []
            while i+j < len(s) and j < numRows:
                temp.append(s[i+j])
                j+=1
            i += j
            split.append(temp)
            k = 0
            temp = []
            while i+k < len(s) and k < numRows-2:
                if k == 0:
                    temp.append(' ')
                temp.append(s[i+k])
                if k == numRows-3:
                    temp.append(' ')
                k+=1
            i += k
            for _ in range(numRows-len(temp)):
                temp.append(' ')
            temp.reverse()
            split.append(temp)
        # output  = [cell for cell in [split[i]] for i in range(numRows)]
        output = []
        for i in range(numRows):
                for item in split:
                    if i < len(item) and item[i] != ' ':
                        output.append(item[i])
        return ''.join(output)
                
            
                
        