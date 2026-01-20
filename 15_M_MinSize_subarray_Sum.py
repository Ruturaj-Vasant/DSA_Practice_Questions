# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: 
# target = 7
# nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: 
target = 11
nums = [1,1,1,1,1,1,1,1]
# Output: 0




#-------------------------------------------
# First attempt the below method though passes the first tests wont work
# l , r = 0 , 1
# subarray = set()

# if target in nums:
#     return 1


# while l<=(len(nums)) and r<(len(nums)):
#     addition = nums[l]+ nums[r]
#     while r<(len(nums)):
#         if addition < target:
#             addition += nums[r]
#             r +=1
#         else:
#             subarray.add(r-l+1)
#             l +=1
#             r = l+1
# sorted(subarray)
# if len(subarray)>1:
#     print(min(subarray))
# else:
#     print(0)

def minsizeSubArray(nums:list[int],target:int)-> int:
    l = 0
    res = float("inf")
    total = 0

    for r in range(len(nums)):

        total += nums[r]

        while total >= target:
            res= min(res,r-l+1)
            total -= nums[l]
            l += 1
            

    if res == float("inf"):
        return 0
    else:
        return res
    
if __name__ == "__main__":
    print(minsizeSubArray(nums, target))