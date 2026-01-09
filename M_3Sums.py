"""
💡 LeetCode 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
------------
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Explanation:
nums[i] + nums[j] + nums[k] == 0 for:
  - (-1) + (-1) + (2) = 0
  - (-1) + (0) + (1) = 0

Constraints:
------------
1 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

Your task:
-----------
Complete the function below.
"""

def threeSum(nums):
    # TODO: Implement the logic
    # Step 1: Sort the array
    nums.sort()

    arr = []
    # Step 2: Use a for loop + two-pointer approach

    # Step 3: Skip duplicates
    # Step 4: Return the list of unique triplets
    pass


# Example usage:
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))  # Expected: [[-1, -1, 2], [-1, 0, 1]]




# nums = [-1,0,1,2,-1,-4]
# nums.sort()

# arr =[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             if nums[i]+nums[j]+nums[k] == 0:
#                 triplet = [nums[i],nums[j],nums[k]]
#                 if triplet not in arr:
#                     arr.append(triplet)
# print(arr)

#Pointer

# for i, v in enumerate(nums):
#     if i >0 and v ==nums[i-1]:
#         continue

#     l, r = i+1, len(nums) -1
#     while l<r:
#         threesums = v + nums[l] + nums[r]
#         if threesums < 0:
#             l += 1
#         elif threesums>0:
#             r -=1
#         else:
#             triplet = [v,nums[l],nums[r]]
#             arr.append(triplet)
#             l += 1
#             while nums[l]==nums[l-1] and l<r:
#                 l += 1

# print(arr)