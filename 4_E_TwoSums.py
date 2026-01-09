# Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1] 



nums=[3,2,4]
target=6


# numbers = [1,2,3,4]
# target = 3


#-------------------------------------
# Brute Force Solution
def brute_force(nums: list[int], target:int)-> list[int]:
    output =[]
    for i in range(len(nums)): # O(n)
        for j in range(i+1,len(nums)): # O(n)
            if nums[i] + nums[j] == target : # O(1)
                return [i,j]
            
# The time complexity is n^2
# enumerated array is indexed array, it is assigned an index
# Java Vs Python Intrepreted language?



#------------------------------------------
# Hash map Solution

# The logic is to store the difference of target and current value in hash map
# Hash_map = {value: index}
# (i,v) = (3,0) (2,1) (4,2)

def Hash_Map(nums: list[int], target:int)-> list[int]:
    hash_map ={}
    
    for i, v in enumerate(nums): # O(n)
        diff = target - v
        if diff in hash_map: # O(1)
            return [i, hash_map[diff]] # O(1) we return current index and index of difference from hash map
        else: # O(1)
            hash_map[v] = i # O(1) while storing value and index in hash map we store value as key and index as value
# The time complexity is O(n)
# The space complexity is O(n) in worst case all elements are stored in hash map    

        
if __name__ == "__main__":
    
    # print(brute_force(nums, target))
    print(Hash_Map(nums,target))