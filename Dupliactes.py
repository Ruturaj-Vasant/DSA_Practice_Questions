nums = [1,2,3,4,1]

if len(nums)!= len(set(nums)):
    print(True)
else:
    print(False)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]: 
            print(True)
            exit()
print(False) #Time complexity is n^2 as two for loops

