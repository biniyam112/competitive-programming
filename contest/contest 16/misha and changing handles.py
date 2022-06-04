changes  = int(input())
handles = {}
for _ in range(changes):
    handle = input().split()
    if handle[0] in handles:
        v = handles.pop(handle[0])
        handles[handle[1]] = v
    else:
        handles[handle[1]] = handle[0]
print(len(handles))
for k,v in handles.items():
    print(v,k)

