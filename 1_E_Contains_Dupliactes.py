# LeetCode Problem 217: Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


nums = [1,2,3,4,1]

# if len(nums)!= len(set(nums)):
#     print(True)
# else:
#     print(False)

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]: 
#             print(True)
#             exit()
# print(False) #Time complexity is n^2 as two for loops

# if len(nums) > len(set(nums)):
#     print(True)
# else:
#     print(False) #Time complexity is n as set is a hash table


# Comming back here forgot how to write set and basic concepts I have to keep 
# resviewing these basic things again and again


def contains_duplicate(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                return True
    return False

def find_duplicates(nums):
    unique_nums = set(nums)
    if len(unique_nums) != len(nums):
        return True
    else:
        return False
if __name__ == "__main__":
    print(find_duplicates(nums))
    print(contains_duplicate(nums))