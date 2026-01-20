# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: 
nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

#---------------------------------------
#Brute force solution 
def brute_force(nums):
    for i,v in enumerate(nums): #O(n)
        if nums.count(v) == 1: #O(n)
            print(v)
            break

#Time complexity is O(n^2)
# space complexity is O(1)
#-----------------------------------------

def hashmap_solution(nums):
     dic = {}
     for i, v in enumerate(nums):
         if v not in dic:
             dic[v] = 1
         else:
             dic[v] += 1
     for i,v in dic.items():
         if v == 1:
             print(i)
             break
#Time complexity is O(n)
#space complexity is O(n)
#-----------------------------------------
def bitwise_solution(nums):
    xor = 0
    for i in nums:
        xor ^= i
    
    return(xor)
#Time complexity is O(n)
#space complexity is O(1)


if __name__ == "__main__":
    brute_force(nums)
    hashmap_solution(nums)
    print(bitwise_solution(nums))