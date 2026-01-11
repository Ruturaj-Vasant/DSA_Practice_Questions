#Question Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: 
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: 
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3

from collections import deque


def Bsf_island(grid: list[list[str]])-> int:
    count = 0

    if not grid:
        return 0
    

    def bsf(r,c):
        search_q = deque()
        visited_points.add((r,c))
        search_q.append((r,c))

        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        while search_q:
            row_q, col_q = search_q.popleft()
            for dr , dc in directions:
                r , c = row_q + dr, col_q + dc

                if (r in range(row) and c in range(col) and grid[r][c] == "1" and (r,c) not in visited_points):
                    visited_points.add((r,c))
                    search_q.append((r,c))




    count = 0
    visited_points = set()
    row = len(grid)
    col = len(grid[0])

    for r in range(row):
        for c in range(col):

            if grid[r][c] == "1" and (r,c) not in visited_points:

                bsf(r, c)
                count += 1
    return count


if __name__ == "__main__":
    # print(len(grid))
    # print(len(grid[0]))
    # print(grid[0][len(grid[0])-1])

    # directions=[[1,0],[-1,0],[0,1],[0,-1]]

    # row = 0
    # col = 0

    # visited_points = set()
    # q = deque()


    # for r , c in directions:
    #     print(r,c)
    #     print(row,col)
    #     visited_points.add((row,col))
    #     print("visited points:",visited_points)
    #     q.append((row,col))
    #     row += r
    #     col += c
    #     print(row,col)
    #     print(q.popleft())
    # print("---------------------------------")     
  
    print(Bsf_island(grid))
