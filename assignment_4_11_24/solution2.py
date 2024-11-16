# Function to find the minimum operations needed
def min_operations_to_max(n, arr):
    # Find the smallest and largest elements in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # If all elements are the same, no operations are needed
    if min_val == max_val:
        return 0
    
    # Count how many times the smallest element appears
    min_count = arr.count(min_val)
    
    # Return the count as the number of operations
    return min_count

# Input the number of test cases
t = int(input("Enter the number of test cases: "))

# Process each test case
results = []
for _ in range(t):
    # Input the size of the array
    n = int(input("Enter the size of the array: "))
    
    # Input the array elements
    arr = list(map(int, input("Enter the array elements: ").split()))
    
    # Store the result for the test case
    results.append(min_operations_to_max(n, arr))

# Print the results
for result in results:
    print(result)
