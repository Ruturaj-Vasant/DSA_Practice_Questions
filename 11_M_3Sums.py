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

nums = [-1, 0, 1, 2, -1, -4]


#-----------------------------------------------
#My Solution

def threeSum_for_loop(nums: list[int])-> list[list[int]]:

    output = []

    for i in range(len(nums)-1): #O(n)
        for j in range(i+1,len(nums)-1): #O(n)
            for k in range(j+1,len(nums)-1): #O(n)
                if nums[i]+nums[j]+nums[k] == 0:
                    triplet = [nums[i],nums[j],nums[k]]
                    triplet.sort() #O(nlogn)
                    if triplet not in output:
                        output.append(triplet)

    return output
# time complexity : O(n^4logn) due to sort function inside the loop
# space complexity : O(m) where m is number of triplets found
                    
def threeSum_pointer(nums: list[int])-> list[list[int]]:
    output =[]
    nums.sort()
    
    for i , v in enumerate(nums):

        if v > 0: # if the value in a sorted array of the first element of the triplet is positive then there will be no solution where the sum is zero
            return output

        if (i) and (v == nums[i-1]): # we continue the loop if the value is similar to  pervious value as the triplets will be the same
            continue

        l , r = i +1 , len(nums)-1 # as it is a sorted array we point left pointer i+1 as we do not wish to use the same element twice and we have explored all teh combinations for elements previous of index i.
        while l <r :
            three_sum = v + nums[l] + nums[r]

            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                output.append([v,nums[l],nums[r]])
                l += 1

                while (l < r) and (nums[l] == nums[l-1]):
                    l += 1
    return output
# Time Complexity O(n^2)


# Example usage:
if __name__ == "__main__":

    # print(threeSum_for_loop(nums))  # Expected: [[-1, -1, 2], [-1, 0, 1]]
    print(threeSum_pointer(nums))




# nums = [-1,0,1,2,-1,-4]
# nums.sort()

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