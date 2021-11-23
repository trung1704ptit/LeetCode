class UnionFind:
    def __init__(self, grid):
        y = len(grid)
        x = len(grid[0])

        self.parents = [0] * (y*x)
        self.count = 0

        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    self.parents[i*x+j] = -1
                    self.count += 1

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] =  x
        self.count -= 1

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        grid_y = len(grid)
        grid_x = len(grid[0])

        uf = UnionFind(grid)

        for i in range(grid_y):
            for j in range(grid_x):
                if grid[i][j] == '1':
                    for k, l in ([1, 0], [-1, 0], [0,1], [0, -1]):
                        ny, nx = i + k, j+k
                        if 0<= ny < grid_y and 0 <= nx < grid_x and grid[ny][nx] == '1':
                            uf.union(i*grid_x+j, ny*grid_x+nx)

        return uf.count