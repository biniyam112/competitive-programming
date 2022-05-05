class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        fir = []
        for i in s:
            if i == '#' and fir:
                fir.pop()
            elif i == '#' and  not fir:
                continue
            else:
                fir.append(i)
        sec = []
        for i in t:
            if i == '#' and sec:
                sec.pop()
            elif i == '#' and not sec:
                continue
            else:
                sec.append(i)
        if len(fir) != len(sec):
            return False
        for i in range(len(fir)):
            if fir[i] != sec[i]:
                return False
        return True