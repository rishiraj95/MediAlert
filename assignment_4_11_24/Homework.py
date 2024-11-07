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
