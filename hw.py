#flip two array elements


def flipElements(arr,n):

    arr2=[]

    for i in range (n - 2):
        arr2 = arr[i]
        print(arr[i])

arr = [13,2]
n = len(arr)

flipElements(arr,n)