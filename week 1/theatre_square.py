m,n,a = list(map(int, input().split()))
side1,mod1 = divmod(m,a)
if mod1 >0:
    side1+=1
side2,mod2 = divmod(n,a)
if mod2 >0:
    side2+=1
print(side1*side2)