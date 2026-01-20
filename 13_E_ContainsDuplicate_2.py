#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: 
nums = [1,2,3,1]
k = 3
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 
#-------------------------------------------------------
# The below soluiton is a solution for set
def containsnearbyDuplicates(nums:list[int],k: int)-> bool:

    sliding_set = set()
    output = False

    for i, v in enumerate(nums): # O(n)
        if v in sliding_set:
            output = True
        else:
            sliding_set.add(v)
        if len(sliding_set) > k:
            sliding_set.remove(nums[i-k]) # The logic is to keep elements with a certain window, once the length of wondow exceeds K we remove the element that was present at index [i-k] i.e k index behind the current iteration.

    return output

#-------------------------------------------------------

def containsduplicatedictionary(nums:list[int],k: int)-> bool:

    dictionary ={}

    for i, v in enumerate(nums):
        if v in dictionary and i - dictionary[v] <= k:
            return True
        dictionary[v] = i
    
    return False

if __name__ == "__main__":
    # print(containsnearbyDuplicates(nums,k))
    print(containsduplicatedictionary(nums,k))