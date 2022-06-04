class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        output = 0
        stack = [a,b,c]
        stack.sort()
        def checkGameOver(lista):
            counter = 0
            for i in lista:
                if i > 0:
                    counter+=1
            if counter > 1:
                return False
            return True
        gameover = checkGameOver(stack)
        while not gameover:
            stack[-1] -= 1
            stack[-2] -= 1
            output += 1
            stack.sort()
            gameover = checkGameOver(stack)
        return output
        
                
        