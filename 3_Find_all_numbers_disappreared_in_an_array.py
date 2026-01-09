#Question: Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]


nums = [4,3,2,7,8,2,3,1]


#-------------------------------------
# My Solution

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    set_nums = set(nums) # O(n) time and space
    dis_nums =[]
    for i in range(1, len(nums)+1): #O(n)
        if i not in set_nums: #O(1)
            dis_nums.append(i)
    return dis_nums

# Time complexity: O(n)
# Space complexity: O(k) k is number of disappeared numbers
# This exceeds time limit on LeetCode


#-------------------------------------
# Optimized Solution
def find_disappeared_numbers_optimized(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        print(nums)
        index = abs(nums[i]) - 1
        print("Index:", index)
        print("Nums at index:", nums[index])
        if nums[index] > 0:
            nums[index] = -nums[index]
            print("Updated Nums at index:", nums[index])
        print("------")
    
    disappeared_numbers = []
    print("Disappeared numbers:", disappeared_numbers)
    for i in range(len(nums)):
        print("Final Nums at index", i, ":", nums[i])
        if nums[i] > 0:
            disappeared_numbers.append(i + 1)
    
    return disappeared_numbers

# Time complexity: O(n)
# Space complexity: O(1) (excluding output list) 
# I do not understand this solution well yet need to reviwe it again



#-------------------------------------
# Using dictionaries optimized solution with extra space

def find_diappeared_numbers_dict(nums: list[int]) -> list[int]:
    dict_nums = {}
    disappeared_numbers = []

    for i in range(1,len(nums)+1): # O(n)
        dict_nums[i] = 0
    for i in nums: # O(n)
        dict_nums[i] = 1
    # for i in dict_nums.keys():
    for i in range(1, len(nums)+1): # O(n)
        if dict_nums[i] == 0:
            disappeared_numbers.append(i)
    
    return disappeared_numbers
# Time complexity: O(n)
# Space complexity: O(n)


if __name__ == "__main__":
    # print(list(i for i in range(1,len(nums)+1) if i not in set(nums))) # Congrations on creating your first one line function
    # print(find_disappeared_numbers(nums)) # This exceeds time limit on LeetCode but I understand this and wrote it on my own
    # print(find_disappeared_numbers_optimized(nums))
    print(find_diappeared_numbers_dict(nums)) # This has similar logic as the optimized solution but uses extra space.