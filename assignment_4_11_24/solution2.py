# Algorithm:
# 1. Define a function min_changes_required that takes an array as input
# 2. Find the minimum element in the array
# 3. Count the number of minimum elements in the array
# 4. Return the number of elements in the array minus the count of minimum elements in the array

def min_changes_required(a):
    minimum = min(a)  # Find the minimum element in the array
    count = a.count(minimum)     # Count the number of minimum elements in the array 
    return len(a) - count    # Return the number of elements in the array minus the count of minimum elements in the array 

t = int(input())

for _ in range(t):
    # Read the size of the array
    n = int(input())
    # Read the array elements
    a = list(map(int, input().split()))
    print(min_changes_required(a))
