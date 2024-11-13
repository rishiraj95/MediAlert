# Function to determine minimum operations required to make minimum element the maximum
def min_operations_to_max(n, arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # If the minimum is already the maximum, no operations are needed
    if min_val == max_val:
        return 0
    
    # Count occurrences of the minimum value
    min_count = arr.count(min_val)
    
    # The number of operations needed is equal to the count of the minimum values
    return min_count

# Read number of test cases
t = int(input("Enter the number of test cases: "))

# Process each test case
results = []
for _ in range(t):
    # Read the size of the array
    n = int(input("Enter the size of the array: "))
    
    # Read the array elements
    arr = list(map(int, input("Enter the array elements: ").split()))
    
    # Determine the result for the current test case
    results.append(min_operations_to_max(n, arr))

# Print all results
for result in results:
    print(result)
