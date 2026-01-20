# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: 
nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

#-----------------------------------------------------
#My Brute force solution
def max_sub_array_forloop(nums) -> int:
    final_sum =0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum1 =0
            for k in range(i,j+1):
                sum1 += nums[k]
            final_sum = max(final_sum,sum1)
    print(final_sum)
#Time complexity is O(n^3)
#Space complexity is O(1)
#-----------------------------------------------------

def max_sub_array_DP(nums) -> int:
    dp = [0] * len(nums)

    for i , v in enumerate(nums): #O(n)
        dp[i] = max(v, dp[i-1]+v) # we are comparing the current value with the sum of current value and previous maximum subarray sum,we can do this because this array has a property that if the previous maximum subarray sum is negative then adding it to current value will only decrease the sum so we take the maximum of current value and current value + previous maximum subarray sum. So we need to know the trick to solve the problem using DP.

    return max(dp)

if __name__ == "__main__":
    max_sub_array_forloop(nums)
    print(max_sub_array_DP(nums))
