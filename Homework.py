def max_subarray(nums):
    # Initialize max_current and max_global with the first element
    max_current = nums[0]
    max_global = nums[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update max_current by including the current element
        max_current = max(nums[i], max_current + nums[i])
        
        # Update max_global if max_current is greater
        if max_current > max_global:
            max_global = max_current
    
    # Return the maximum subarray sum
    return max_global

# Example usage
example_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", max_subarray(example_array))
