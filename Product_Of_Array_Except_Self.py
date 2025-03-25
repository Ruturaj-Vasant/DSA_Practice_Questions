nums = [1,2,4,6]

product = 1

output =[] # Time complexity is O(n^2)

for i,v1 in enumerate(nums):
    print(i,v1)
    for j,v2 in enumerate(nums):
        print(j,v2)
        if i ==j:
            continue
        else:
            product*= v2
    output.append(product)
    
    product = 1

print(output) 

res = [1] * len(nums)

prefix = 1

for i in range(len(nums)):
    print(i)
    res[i] = prefix # = diffrence
    prefix *= nums[i]
    postfix = 1
for i in range(len(nums) - 1, -1 ,-1):
    print(i)
    res[i] *= postfix # *= difference as we come back multiplying
    postfix*=nums[i]
print(res) # time complexity is O(n)
# for loop (start,stop,step)
# prefix is just multiplying as we go and saving the number
# postfix is we take the number present in the array res and multiply 
# it with the calculated postfix
# 
