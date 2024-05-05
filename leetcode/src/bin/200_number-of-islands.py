'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
'''

from typing import List
from pprint import pprint
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m,n = len(grid), len(grid[0])
        def dfs(grid, r, c, marked, conn_group):
            if grid[r][c] == '0':
                return 
            if grid[r][c] == '1':
                marked[r,c] = 1
                conn_group.append((r,c))
            for d in directions:
                nr,nc = r + d[0],c + d[1] 
                if 0 <= nr < m and 0 <= nc < n:
                    if (nr,nc) not in marked:
                        dfs(grid, nr, nc, marked, conn_group)
        
        #marked = collections.defaultint()
        marked = {}
        conn_groups = []
        for r in range(0,m):
            for c in range(0,n):
                if (r,c) not in marked:
                    group = []
                    dfs(grid, r, c, marked, group)
                    if group:
                        conn_groups.append(group) 

        return len(conn_groups)


if __name__ == "__main__":
    '''
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    '''
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    pprint(grid)
    sol = Solution()
    ans = sol.numIslands(grid)
    print(f"ans:{ans}")


