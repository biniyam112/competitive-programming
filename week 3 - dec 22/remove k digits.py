
def removeKdigits( num: str, k: int) -> str:
    monostack = []
    for i in num:
        if not monostack or int(monostack[-1]) <= int(i) or k==0:
            monostack.append(i)
        else:
            while monostack and int(monostack[-1]) > int(i) and k > 0:
                monostack.pop()
                k-=1
            monostack.append(i)
    if not monostack[:len(monostack)-k]:
            return "0"
    return str(int(''.join(monostack[:len(monostack)-k])))





removeKdigits()