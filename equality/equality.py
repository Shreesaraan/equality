def equality(A):
    maxi=float('-inf')
    time_taken=0
    for i in range(len(A)):
        if A[i]>maxi:
            maxi=A[i]
    for i in range(len(A)):
        time_taken+=maxi-A[i]
    return time_taken

A=list(map(int,input("Enter the Array Elements: ").split()))
print(equality(A))