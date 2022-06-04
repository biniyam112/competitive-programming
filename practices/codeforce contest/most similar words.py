cases = int(input())
for _ in range(cases):
    temp =  input().split()
    temp = [int(x) for x in temp]
    words = []
    for i in range(temp[0]):
        words.append(input())
    mindiff =  float('inf')
    for word1 in range(len(words)):
        for word2 in range(word1+1,len(words)):
            diff = 0
            for i in range(temp[1]):
                diff+=abs(ord(words[word1][i])-ord(words[word2][i]))
            mindiff = min(mindiff,diff)
    print(mindiff)
