cases = int(input())
for _ in range(cases):
    # print('\n\n', '------------------')
    n = int(input())
    candies = input().split()
    candies = [int(x) for x in candies]
    if n == 1 and candies[0] != 0:
        print(0)
    else:
        alice_s = {}
        bob_s = {}
        a_sum = 0
        b_sum = 0
        a = 0
        b = len(candies)-1
        max_sum = 0
        while a <= b:
            # print('the max sum is ', max_sum)
            if a_sum >= b_sum:
                b_sum += candies[b]
                bob_s[b_sum] = len(candies)-b
                if b_sum in alice_s:
                    max_sum = alice_s[b_sum] + len(candies)-b
                b -= 1
            else:
                a_sum += candies[a]
                alice_s[a_sum] = a+1
                if a_sum in bob_s:
                    max_sum = bob_s[a_sum] + a+1
                a += 1
        print(max_sum)
