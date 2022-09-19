input()
nums = input().split()
nums = [int(x)for x in nums]
nums.sort()
bits = '0' * (len(bin(max(nums)))-2)
count = len(bits)
bits = int(bits, 2)
for num in nums:
    bits = bits & num
print(bin(bits))
bits = bin(bits)[2:]
while len(bits) < count:
    bits = '0' + bits   
print(bits)
inv = ''
for i in bits:
    if i == '0':
        inv += '1'
    else:
        inv += '0'
print(int(inv, 2))
