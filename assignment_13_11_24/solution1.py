# Define the function to determine if we can reduce the array to one element
def can_reduce_to_one_element(n, k, arr):
    # If the array has only one element, it's already the final form we want
    if n == 1:
        return "YES"

    # Sort the array to allow easy pairing of smallest and largest elements
    arr.sort()

    # Initialize two pointers: one starting from the beginning and one from the end of the array
    left, right = 0, n - 1

    # Continue until there are elements to process
    while left < right:
        # If the sum of the smallest and largest element is less than or equal to K
        if arr[left] + arr[right] <= k:
            # Remove the smallest element by moving the left pointer
            left += 1
            # If we've reduced the array to one element, return "YES"
            if left == right:
                return "YES"
        else:
            # If the sum exceeds K, try with a smaller element by moving the right pointer
            right -= 1
    
    # If we can't reduce to one element, return "NO"
    return "NO"

# Read the number of test cases
t = int(input().strip())

# For each test case
for _ in range(t):
    # Read N and K
    n, k = map(int, input().strip().split())
    # Read the array A
    arr = list(map(int, input().strip().split()))

    # Call the function and print the result for each test case
    print(can_reduce_to_one_element(n, k, arr))
