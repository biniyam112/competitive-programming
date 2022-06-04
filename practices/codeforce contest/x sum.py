cases = int(input())
for _ in range(cases):
    temp = input().split()
    n = int(temp[0])
    m = int(temp[1])

    board= []
    for _ in range(n):
        row = input().split()
        row = [int(x) for x in row]
        board.append(row)
    
    def upright(i,j):
        attack  = 0
        while 0 <= i < len(board) and 0<= j < len(board[0]):
            attack+=board[i][j]
            i-=1
            j+=1
        return attack
        
    def downright(i,j):
        attack = 0
        while 0 <= i < len(board) and 0<= j < len(board[0]):
            attack+=board[i][j]
            i+=1
            j+=1
        return attack
    def upleft(i,j):
        attack = 0
        while 0 <= i < len(board) and 0<= j < len(board[0]):
            attack+=board[i][j]
            i-=1
            j-=1
        return attack
    def downleft(i,j):
        attack = 0
        while 0 <= i < len(board) and 0<= j < len(board[0]):
            attack+=board[i][j]
            i+=1
            j-=1
        return attack
    def setupdown(i,j,value):
        while 0 <= i < len(board) and 0<= j < len(board[0]):
            i-=1
            j-=1
            updown[(i,j)] = value
        while 0 <= i < len(board) and 0<= j < len(board[0]):
            i+=1
            j+=1
            updown[(i,j)] = value
        

    output = 0
    updown = {}
    rightleft = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            uldr = upleft(i-1,j-1)+downright(i+1,j+1)
            urdl = upright(i-1,j+1)+downleft(i+1,j-1)
            output = max(output,uldr+urdl+ board[i][j])
    print(output)
   
