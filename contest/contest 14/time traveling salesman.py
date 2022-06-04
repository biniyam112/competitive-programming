size = int(input())
nums = input().split()
profit = {}
def dp(index):
    profit[index] = 0
    