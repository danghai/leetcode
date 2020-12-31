class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:  # Obstacle at first point [0,0]
            return 0
        obstacleGrid[0][0] = 1
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(1, row):  # Mark first column by 1 before obstacle, and by 0 after obstacle
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0)

        for j in range(1, col):  # Mark first row by 1 before obstacle, and by 0 after obstacle
            obstacleGrid[0][j] = int(obstacleGrid[0][j-1] == 1 and obstacleGrid[0][j] == 0)

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 0: # See obstacle
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[row-1][col-1]
