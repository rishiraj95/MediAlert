def can_reduce_to_one_element(N, K, A):
    # If only one element, it's trivially YES
    if N == 1:
        return "YES"
    
    # Sort the array to check pairs efficiently
    A.sort()
    
    # Check if the smallest and largest elements form a valid pair
    if A[0] + A[-1] <= K:
        return "YES"
    else:
        return "NO"

# Input reading
T = int(input())  # Number of test cases
for _ in range(T):
    N, K = map(int, input().split())  # Array size and constant K
    A = list(map(int, input().split()))  # The array A
    
    # Get the result for this test case and print it
    result = can_reduce_to_one_element(N, K, A)
    print(result)
