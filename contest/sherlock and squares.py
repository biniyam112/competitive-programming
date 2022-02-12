import math


def squares(a, b):
    # Write your code here
    counter = 0
    a = math.sqrt(a)
    b = math.sqrt(b)
    if b == int(b):
        counter+=1
    for i in range(math.ceil(a),math.ceil(b)):
        counter+=1
    return counter