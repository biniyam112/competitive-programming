topics = int(input())
teacher_int = input().split()
student_int = input().split()
diff = [int(teacher_int[i])-int(student_int[i]) for i in range(topics)]
diff.sort()
index = 0
pairs = 0
found = False
for i in range(1,len(diff)):
    if not found:
        index = i-1
    while index >= 0:
        if diff[i] + diff[index] > 0:
            found = True
            index -= 1
        else:
            break
    pairs+=i-index-1
print(pairs)

    