arr = [10, 20, 30, 40, 50]



def find_max(arr):

    max_arr = arr[0]

    for i in arr:
        if max_arr < i:
            max_arr = i
    return max_arr

def find_max_space_comp_0(arr):
    for i in range(1, len(arr)):
        if arr[0]<arr[i]:
            arr[0]=arr[i]
    return arr[0]

print(arr)
print(find_max(arr))
print(arr)
print(find_max_space_comp_0(arr))
print(arr)