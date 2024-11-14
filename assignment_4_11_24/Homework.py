# Homework
# Maximum Subarray problem Kadane’s algorithm

# Input1
# 5
# 1 2 3 -2 5
# Output1
# 9
# Input2
# 4
# -1 -2 -3 -4 
# Output2
# -1

# stores the size of array in n
n=int(input())

# stores the elements of a list in integer type with variabe l 
l=list(map(int,input().split()))

# stores 1st element of a list in global_variable and local_variable
local_variable_max=l[0]
global_variable_max=l[0]

#iterates through list from 2nd element
for i in range(1,n):

    # stores the sum of contiguous array
    local_variable_max=local_variable_max+l[i]

    if local_variable_max<l[i]:
        local_variable_max=l[i]
    if global_variable_max<local_variable_max:
        global_variable_max=local_variable_max

# generates the max subarray
print(global_variable_max)
def max_subarray_sum(arr):
    # Initializing two variables.
    # max_current is the maximum sum of the subarray that ends at the current position.
    # max_global keeps track of the maximum sum encountered so far across all subarrays.
    max_current = max_global = arr[0]

    # Looping through each element in the array starting from the second element.
    for i in range(1, len(arr)):
        # Updating max_current to be either the current element alone (new subarray starts here).
        # Or add the current element to the previous max_current (extend previous subarray).
        max_current = max(arr[i], max_current + arr[i])

        # Updating max_global if max_current is greater than the current max_global.
        max_global = max(max_global, max_current)

    return max_global

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum is:", max_subarray_sum(arr))
