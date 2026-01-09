# Question: How many numbers are smaller than the current number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1,2,2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1,2 and 2).
# Example 2:
# Input: 
# nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

nums = [8,1,2,2,3]

#-------------------------------------
# My Solution

def howManySmallerNumbers(nums: list[int])-> list[int]:

    output = [] # define output list

    for i in range(len(nums)): # O(n)
        count = 0
        for j in range(len(nums)): # O(n)
            if  nums[i]>nums[j]: # O(1)
                count += 1
                # print("count for:",nums[i],nums[j],"is",count)
        output.append(count)

    return output
# Time complexity is n^2 as we use two loops
# Space complexity is O(1) as we are not using any extra space except output list

#-------------------------------------
# Method 2 sort and use dictionary
def howManySmallerNumbers_v2(nums: list[int])-> list[int]:

    temp = sorted(nums) # O(nlogn) we sort the list
    # print(temp)
    dictionary={} # we create a dictionary 
    output =[]

    for i, num in enumerate(temp):  # O(n) we are iterating through the list
        # print(i,num)
        if num not in dictionary: # we check if the num is in dict or not, this is vital for keeping the correct count of the numbers less than current number.
            dictionary[num] = i # if not then we add to dictionary

    # print(dictionary)

    for i in nums: #  O(n) now we are traverse through the original nums list
        output.append(dictionary[i]) # while traversing we find the index from the dictionary and store it in the output this solution only works because we sort the list earlier and when sorted the index of the list becomes the count of the numbers less than the current number

    return output
# Time complexity is O(nlogn) due to sorting
# Space complexity is O(n) due to dictionary and output list

#---------------------------------------
# Method 3

def howManySmallerNumbers_v3(nums: list[int])-> list[int]:
    temp = sorted(nums) # O(nlogn) we sort the list
    output_new = []
    for i in nums: # O(n)
        output_new.append(temp.index(i)) # O(n) index function itself is O(n)
        print("output_new", output_new, "i:", i,"index:", temp.index(i))
    return output_new
# Time complexity is O(nlogn) 
# output_new = [temp.index(i) for i in nums]
# print(output_new)

#-------------------------------------
# Method 4 List comprehension version of method 3
def howManySmallerNumbers_v4(nums: list[int])-> list[int]:
    temp = sorted(nums)
    return [temp.index(i) for i in nums]
# Time complexity is O(nlogn)
# Space complexity is O(n)

if __name__ == "__main__":
    # print(howManySmallerNumbers(nums))
    # print(howManySmallerNumbers_v2(nums))
    # print(howManySmallerNumbers_v3(nums))
    print(howManySmallerNumbers_v4(nums))

