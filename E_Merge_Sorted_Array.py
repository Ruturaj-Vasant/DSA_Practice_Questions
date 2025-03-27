import bisect

# Learned nums[index1:Index2] slicing
# practiced binary search method was able to identify and apply it. Good
# Position shifting while nums1[pos+1:m+i+1] = nums1[pos:m+i] replaces the m+i th zero 
# if we did nums1[pos+1:len(nums1)] = nums1[pos:Len(nums1)] we could preserve it if we 
# want(future reference)

nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3



for i in range(n):
    pos = bisect.bisect_left(nums1[:m+i],nums2[i])
    nums1[pos+1:m+i+1] = nums1[pos:m+i]
    nums1[pos] = nums2[i]
    
print(nums1)