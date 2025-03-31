nums = [2,20,4,10,3,4,5]

num1 = sorted(set(nums)) 

count=1
max_count = 1
if num1:
    for i in range(1,len(num1)):
        if num1[i] == (num1[i-1]+1):
            count+=1 
            max_count=max(count,max_count)
        else:
            count = 1
else:
    max_count=0
    
print(max_count)

num2 = set(nums)

max_count2=0

for i in num2:
    if (i -1) not in num2:
        count2 =1
        while(i+count2) in num2:
            count2+=1
        max_count2=max(count2,max_count2)
print(max_count2)

