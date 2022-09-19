items = int(input())
score_tot = {}
maxscore = 0
winner = ''
for _ in range(items):
    score = input().split()
    if  score[0] in score_tot:
        score_tot[score[0]] += int(score[1])           
    else:
        score_tot[score[0]] = int(score[1])
    maxscore = 0
    for k,v in score_tot.items():
        if v > maxscore:
            maxscore = v
            winner = k
    if score_tot[score[0]] > maxscore:
            maxscore = score_tot[score[0]]
            winner = score[0]

print(winner)