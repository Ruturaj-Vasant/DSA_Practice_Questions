#num= [[1,1],[3,4],[-1,0]]
num= [[1,1],[3,4],[-1,0]]
#print(num[1])

#Below is the calculated

# difference=[]
# tml =0
# for i in range(len(num)-1):
#     print(num[i])
#     diff= [num[i+1][0]- num[i][0],num[i+1][1] - num[i][1]]
#     if (num[i+1][0]- num[i][0]== num[i+1][1] - num[i][1]):
#         min_len = abs(num[i+1][0]- num[i][0])
#     else:
#         min_len= abs(min(diff)) + abs((diff[1] - diff[0]))
#     print(diff)
#     print(min_len)
#     tml += min_len
#    # difference.append(diff)
    
# print(difference)
# print(tml)
x1,y1 =num.pop()
print(x1,y1)