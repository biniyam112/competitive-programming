class Solution:
    def myAtoi(self, s: str) -> int:
        output = []
        for i in range(len(s)):
            if len(output) ==  0 and (ord(s[i]) == 32):
                continue
            elif len(output) == 0 and (ord(s[i]) == 45 or ord(s[i]) == 43):
                output.append(s[i])
            elif ord(s[i]) > 57 or ord(s[i]) < 48:
                break
            else:
                output.append(s[i])
        if len(output) == 0 or (len(output) == 1 and (output[0] == '-' or output[0] == '+')):
            return 0
        value =  int(''.join(output))
        if value > 2147483647:
            return 2147483647
        if value < -2147483648:
            return -2147483648
        return value

            
        