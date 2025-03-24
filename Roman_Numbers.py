s = "IV"

hash_map = {}
hash_map['I']=1
hash_map['V']=5
hash_map['X']=10
hash_map['L']=50
hash_map['C']=100
hash_map['D']=500
hash_map['M']=1000

print(hash_map)

arr = list(s)

print(arr)
print(len(arr))

val = 0

for i in range(len(arr)-1):
    print(hash_map[arr[i]])
    if hash_map[arr[i+1]] > hash_map[arr[i]]:
        val = val - hash_map[arr[i]]
    else:
        val += hash_map[arr[i]]
    val += hash_map[arr[-1]]

# for i , v in enumerate(arr):
#     # print(i,v)
#     print(hash_map[arr[i]])
#     if i+1 < len(arr) and hash_map[arr[i+1]] > hash_map[arr[i]]:
#         val = val - hash_map[arr[i]]
#     else:
#         val += hash_map[arr[i]]
    
    


print(val)

# What I learnt was if I+1 > I in roman we substract or else we add
# splitting str and storing it in arr arr = list(str)
# define a hashmap = {'I' = 1, 'V' = 5}