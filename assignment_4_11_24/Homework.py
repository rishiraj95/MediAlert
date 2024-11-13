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
