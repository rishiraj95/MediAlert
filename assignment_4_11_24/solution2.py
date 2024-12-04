def solve():
    T = int(input())  # Read number of test cases
    for _ in range(T):
        N = int(input())  # Read the size of the array
        A = list(map(int, input().split()))  # Read the array elements
        
        M = min(A)  # Find the minimum value in the array
        # Count how many elements are greater than M
        count_greater = sum(1 for x in A if x > M)
        
        # Output the number of operations needed
        print(count_greater)

# Call the solve function to process the input
solve()
