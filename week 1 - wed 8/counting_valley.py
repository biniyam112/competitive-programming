def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valleyCount = 0
    for i in range(steps):
        if path[i] == 'D':
            altitude-=1
            
        else :
            altitude+=1
            if (altitude  == 0) and (i >0):
                valleyCount +=1
    return valleyCount
        