class Solution(object):
    def uniquePaths(self, m, n):
        path = []
        for i in range(n):
            path.append([1]*m)
        for i in range(1, n):
            for j in range(1, m):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[-1][-1]

