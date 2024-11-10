# Maximum Subarray problem Kadane’s algorithm

# Algorithm:
# 1. define a function maxSubArraySum that takes an array of integers as input
# 2. Initialize max_current and max_global to the first element of the array    
# 3. Initialize max_start and max_end to 0
# 4. Iterate through the array from the second element
# 5. Calculate max_current as the maximum of the current element and the sum of the current element and max_current
# 6. Update max_global if max_current is greater than max_global
# 7. Update max_start and max_end if max_current is greater than max_global
# 8. Return max_global


def maxSubArray(nums):
        # Create an array...
        arr = []
        arr.append(nums[0])
        # Initialize the max sum...
        maxSum = arr[0]
        # Traverse all the element through the loop...
        for i in range(1, len(nums)):
            # arr[i] represents the largest sum of all subarrays ending with index i
            # then its value should be the larger one between nums[i]
            # arr[i-1] + nums[i] (largest sum plus current number with using prefix)
            # calculate arr[0], arr[1]…......., arr[n] while comparing each one with current largest sum
            arr.append(max(arr[i-1] + nums[i], nums[i]))
            # if arr[i] > maxSum then maxSum = arr[i].
            if arr[i] > maxSum:
                maxSum = arr[i]
        return maxSum       # Return the contiguous subarray which has the largest sum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]     # input array
max_sum = maxSubArray(arr)   # call the function max_subarray_sum
print("Maximum subarray sum:", max_sum)    # print the maximum subarray sum

