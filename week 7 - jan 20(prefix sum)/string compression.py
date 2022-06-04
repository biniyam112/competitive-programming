from typing import List


def compress(self, chars: List[str]) -> int:
    s = ''
    start=0
    end = 0
    while end < len(chars):
        if chars[start] != chars[end]:
            start+=1
            end+=1
    else:
        while chars[start] == chars[end]:
            end+=1
            if end == len(chars):
                break
        s += chars[start]
        if end-start > 1:
            s+= str(end-start)
        start = end
    for i in range(len(s)):
        chars[i] = s[i]
    return len(s)