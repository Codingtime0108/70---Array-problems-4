def equilibriumPoint(arr):
    leftSide = 0
    rightSide = 0
    n = len(arr)

    for i in range(n):
        leftSide = 0
        rightSide = 0

        for j in range(i):
            leftSide += arr[j]

        for j in range(i+1,n):
            rightSide += arr[j]

        if leftSide == rightSide:
            return 1
        
    return -1
arr = [-4,6,2,0,0,1,1]
print("Element :",arr[equilibriumPoint(arr)])
