# Function to calculate minimum operations to make the minimum value the maximum in the array
def min_operations_to_max(n, arr):
    # Find the minimum value in the array
    min_value = min(arr)
    
    # Count how many elements are greater than the minimum value
    operations = sum(1 for x in arr if x > min_value)
    
    return operations

# Input and Output handling
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    # Read number of elements in the array
    n = int(input())
    # Read the array elements
    arr = list(map(int, input().split()))
    
    # Calculate the result for the current test case
    results.append(min_operations_to_max(n, arr))

# Output each result for the test cases
for result in results:
    print(result)
