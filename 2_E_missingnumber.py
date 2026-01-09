#Question: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


#-------------------------------------
# Working of Enumerate funciton
#-------------------------------------
# fruits = ['apple' , 'banana', "orange"]

# for index, fruits in enumerate(fruits):
#     print(index,fruits)



#-------------------------------------
# Working of range function
# for i in range(3): # in range function (3) index starts from 0,1,2. Index starts at 0 and stops at 2
#     print("index", i)

#-------------------------------------


#-------------------------------------
# Different Nums
# nums = [3, 0, 1]
# nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]


#----------------------------
# My first solution 
def missing_num(nums: list[int]) -> int:
    for i in range(len(nums)+1): # O(n)
        if i in nums: # i in nums O(n)
            continue
        else:
            return i

# time complexity O(n^2)
# Space complexity: O(1) (constant)
#-----------------------------

#-------------------------------------
# Second Solution
def missing_num_enumerate(nums: list[int]) -> int:
    nums.sort() #Python uses Timsort O(n log n) (worst/average)
	#Space: O(1) extra 

# print(nums)

# Below we try to match index with number after sorting and return the missing number by checking if index matches number. After sorting the index should match the number at that index. 

    for index, number in enumerate(nums): #O(n)
        if index != number:  #O(1)
            return (number-1) #O(1)

# This is for the case when the missing number is the last number
        if number == len(nums)-1: #O(1)
            return (number+1)

# time complexity: O(n log n) due to sorting
# Space complexity: O(1) (constant)
#-------------------------------------



#-------------------------------------
# Optimal Solution using sum formula
def missing_num_sum(nums: list[int]) -> int:

# Below we are finding the expected sum of the range and substracting it from the actual sum of the list. The difference should be the missing number.
    return(sum(range(len(nums)+1)) - sum(nums)) #O(n) to calculate sum of nums list and O(1) to create range and O(n)calculate its sum.

# time complexity: O(n)
# Space complexity: O(1) (constant)
#-------------------------------------


if __name__ == "__main__":

    print("Missing Number:",missing_num(nums))
    print("Missing Number using enumerate:",missing_num_enumerate(nums))
    print("Missing Number using sum formula:",missing_num_sum(nums))
