arr = [10, 20, 4, 45, 99]
print(arr)
j = "null"

n = len(arr)

for j in range(n):
    print()
    print('')
    for i in range(0, n-j-1):
        print(arr[i],end=" ")
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print()
print(arr[1])

# arr.sort()
# print(arr)
# arr.reverse()
# print(arr)
# print(arr[1])