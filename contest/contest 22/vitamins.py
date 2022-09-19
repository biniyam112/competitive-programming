from sympy import minpoly


n = int(input())
comb = {}
for _ in range(n):
    juice = input().split()
    if juice[1] not in comb:
        comb[juice[1]] = int(juice[0])
    else:
        comb[juice[1]] = min(comb[juice[1]], int(juice[0]))
minPrice = float('inf')

# for k, v in comb.items():
#     if len(k) == 3 and v < minPrice:
#         minPrice = v
#     for k2, v2 in comb.items():
#         if set(k+k2) == 3 and v+v2 < minPrice:
#             minPrice = v+v2
# print(minPrice)
