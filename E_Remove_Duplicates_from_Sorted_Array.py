#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

# use of list(set(nums)) takes a list and converts back into a list without duplicates
l=0
#r=0

for r in range(len(nums)):
    if nums[l] == nums[r]:
        #r+=1
        continue
    else:
        l+=1
        nums[l]=nums[r]

print(l+1)