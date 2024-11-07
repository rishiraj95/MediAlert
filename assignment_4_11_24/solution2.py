# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the size of the array
    N = int(input())
    # Read the array elements
    A = list(map(int, input().split()))
    
    # Find the minimum value in the array
    M = min(A)
    
    # Count how many elements are greater than the minimum value
    count_greater = sum(1 for x in A if x > M)
    
    # Output the result (number of operations needed)
    print(count_greater)
