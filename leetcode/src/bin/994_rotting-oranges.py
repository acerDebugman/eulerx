'''
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
示例 1：
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
'''

from typing import List
from pprint import pprint
from collections import deque

class Solution:
    # 多源的层次遍历
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        m,n = len(grid),len(grid[0])
        def dfs(grid, r, c, visited, conn_set, rot_set):
            if grid[r][c] == 0:
                return 
            if grid[r][c] == 1 or grid[r][c] == 2:
                visited[r,c] = -1
                if grid[r][c] == 1:
                    conn_set.append((r,c))
                if grid[r][c] == 2:
                    rot_set.append((r,c))
            for d in dirs:
                nr,nc = r+d[0],c+d[1]
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                    dfs(grid, nr, nc, visited, conn_set, rot_set) 

        def count_step(grid, rot_points) -> int:
            ans_max = 0
            s = deque()
            s.extend(rot_points)
            # 这里用q就行，不需要用set
            #print(q)
            #s = set(rot_points)
            while s:
                print(s)
                #print(ans_max)
                tmp = []
                #for e in s:
                while s:
                    e = s.popleft()
                    for d in dirs:
                        nr,nc = e[0]+d[0], e[1]+d[1] 
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                            tmp.append((nr,nc))
                            grid[nr][nc] = 2
                #s = set(tmp)
                s.extend(tmp)
                if tmp:
                    ans_max+=1
            return ans_max

        rot_points = []
        visited = {}
        for r in range(0, m):
            for c in range(0, n):
                if (r,c) not in visited:
                    conn_set, rot_set = [],[]
                    dfs(grid, r, c, visited, conn_set, rot_set)
                    # 另外一种判断-1的方法是最后在扫描是否还有1的节点也可以！
                    if conn_set and not rot_set:
                        return -1
                    if rot_set:
                        rot_points.extend(rot_set)

        if not rot_points:
            return 0
        
        return count_step(grid, rot_points)

    # 用曼哈顿距离计算时间的方式错误了，只能按照深度+回溯的方式遍历
    def orangesRotting1(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        m,n = len(grid),len(grid[0])
        def dfs(grid, r, c, visited, conn_set, rot_set):
            if grid[r][c] == 0:
                return 
            if grid[r][c] == 1 or grid[r][c] == 2:
                visited[r,c] = -1
                if grid[r][c] == 1:
                    conn_set.append((r,c))
                if grid[r][c] == 2:
                    rot_set.append((r,c))
            for d in dirs:
                nr,nc = r+d[0],c+d[1]
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                    dfs(grid, nr, nc, visited, conn_set, rot_set) 
        
        visited = {}
        max_m = 0
        for r in range(0, m):
            for c in range(0, n):
                if (r,c) not in visited:
                    conn_set, rot_set = [],[]
                    dfs(grid, r, c, visited, conn_set, rot_set)
                    if conn_set and not rot_set:
                        return -1
                    for r1,c1 in rot_set:
                        for r2,c2 in conn_set:
                            max_m = max(max_m, abs(r2 - r1) + abs(c2 - c1))

        return max_m

if __name__ == "__main__":
    '''
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    '''
    #grid = [[2,1,1],[0,1,1],[1,0,1]]
    #grid = [[0,2]]
    #grid = [[1,2]]
    #grid = [[0,2,2]]
    grid = [[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
    pprint(grid)
    sol = Solution()
    ans = sol.orangesRotting(grid)
    print(f"ans:{ans}")

