#Question Link: https://leetcode.com/problems/minimum-time-visiting-all-points/
# Question: Minimum Time Visiting All Points
# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. 
# The points are visited in the order they appear in the array.
# You are allowed to move according to these rules:
# In one second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally (which is one unit vertically and one unit horizontally in one second).
# Return the minimum time in seconds to visit all points.
# Example 1:
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7 
# Explanation: One optimal path is as follows:
# From [1,1] to [3,4] : 3 seconds (1 diagonal move to [2,2], 1 diagonal move to [3,3], 1 vertical move to [3,4])
# From [3,4] to [-1,0] : 4 seconds (1 diagonal move to [2,3], 1 diagonal move to [1,2], 1 diagonal move to [0,1], 1 diagonal move to [-1,0])
# Example 2:
# Input: points = [[3,2],[-2,2]]
# Output: 5 

num= [[1,1],[3,4],[-1,0]]



#---------------------------------------------


def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    time = 0
    x1 , y1 = points.pop() # O(1)
    while points: # O(n)
        x2,y2 = points.pop() # O(1)
        time += max(abs(x1-x2),abs(y1-y2)) # O(1)
        x1, y1 = x2, y2
    
    return time
# Time complexity is O(n) as we traverse through the list once
# Space complexity is O(1) as we are not using any extra space except variables


if __name__ == "__main__":
    print(minTimeToVisitAllPoints(num))




#---------------------------------------------
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
# x1,y1 =num.pop()
# print(x1,y1)