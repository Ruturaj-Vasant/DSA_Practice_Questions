import bisect
nums = [1,3,5,6] 
target = 0

for i,v in enumerate(nums):
    if v == target:
        print (i)
        break
    elif v > target:
        print(i)
        break

if target > nums[len(nums)-1]:
    print(len(nums))

# Time complexity is O(n) as we are iterating through the whole list.
# as the list is sorted we can use binary search

print(bisect.bisect_left(nums,target))

def binary_search(nums,target):

    low =0
    high = len(nums) -1

    while low <= high:
        mid = (low + high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high = mid -1
        else:
            low = mid +1
    return low

print(binary_search(nums,target))