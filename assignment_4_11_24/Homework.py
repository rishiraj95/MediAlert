# Input the size of the array
n = int(input())

# Input the array elements as a list of integers
l = list(map(int, input().split()))

# Initialize local and global maximum with the first element
local_variable_max = l[0]
global_variable_max = l[0]

# Iterate through the array starting from the second element
for i in range(1, n):
    # Update the local maximum (current subarray sum)
    local_variable_max = max(l[i], local_variable_max + l[i])
    
    # Update the global maximum if the current local max is greater
    global_variable_max = max(global_variable_max, local_variable_max)

# Output the maximum subarray sum
print(global_variable_max)
