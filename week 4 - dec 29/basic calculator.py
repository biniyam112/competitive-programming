
def calculate( s: str) -> int:
    stack = []
    i = 0
    while i < len(s):
        num = ''
        while s[i] != '/' and s[i] !='*' and s[i] !='+' and s[i] !='-':
            num += s[i]
            i+=1
            if i == len(s):
                break
        if num != ''  and i ==len(s):
            stack.append(num)
        if i == len(s):
            break
        if s[i] == '/' or s[i] =='*' or s[i] =='+' or s[i] =='-':
            stack.append(num)
            num = ''
            stack.append(s[i])
            i+=1
    i = 0
    stack1 = []
    while i < len(stack):
        if  stack[i] !='/' and stack[i] !='*' :
            stack1.append(stack[i])
            i+=1
        elif stack[i] == '*':
            stack1.append(str(int(stack1.pop()) * int(stack[i+1])))
            i+=2
        elif stack[i] == '/':
            stack1.append(str(int(stack1.pop()) // int(stack[i+1])))
            i+=2
    value = int(stack1[0])
    if len(stack1) == 1:
        value= int(stack1[0])
    for i in range(1,len(stack1),2):
        if stack1[i] == '+':
            value += int(stack1[i+1])  
        elif stack1[i] == '-':
            value -= int(stack1[i+1])  
    return int(value)
    
    
calculate(" 3+5 /")