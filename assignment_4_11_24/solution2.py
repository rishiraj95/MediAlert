#The number of test cases
T = int(input()) 

for _ in range(T):
    #The size of the array
    N = int(input())
    
    #The elements of the array
    A = list(map(int, input().split()))
    
    min_val = min(A)
    X = 0
    for num in A:
        if num > min_val:
            X += 1
    print(X)
