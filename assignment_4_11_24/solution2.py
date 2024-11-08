def min_to_max_operations(N, A):
    # N: Number of items in the array
    # A: List of integers representing the prices of the items
    
    # Find the initial minimum value M in the array A
    M = min(A)
    
    # Calculate the number of operations needed
    operations = 0
    for value in A:
        # Check if the current value is greater than the minimum value M
        # If it is greater, we need to perform an operation to change it
        if value > M:
            operations += 1
    
    return operations

# Read number of test cases
T = int(input("Enter the number of test cases: "))
results = []

for _ in range(T):
    # Read N (size of the array)
    N = int(input("Enter the size of the array: "))
    
    # Read the array of N integers
    A = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    # Determine the number of operations required for this test case
    results.append(min_to_max_operations(N, A))

# Print the results for all test cases
for result in results:
    print(result)