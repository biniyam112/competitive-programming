def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True


cases = int(input())
for _ in range(cases):
    s = input()
    notPalindrome = False
    for i in s:
        if i != 'a':
            notPalindrome = True
            print('YES')
            pre = 'a'+s
            if isPalindrome(pre):
                print(s+'a')
            else:
                print(pre)
            break
    if  not notPalindrome:
        print('NO')
    