class Solution:
    def sortSentence(self, s: str) -> str:
        wordlist = s.split(' ')
        order = ['']*len(wordlist)
        for i in range(len(wordlist)):
            order[int(wordlist[i][-1])-1] = wordlist[i][0:len(wordlist[i])-1]
        return ' '.join(order)

