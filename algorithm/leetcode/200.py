class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            grid[x][y] = 0
            for i in range(len(dx)):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == '1':
                    dfs(nx, ny)

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    answer += 1
                    dfs(i, j)


        return answer

# class Solution:
#     def dfs(self, grid, x, y):
#         dx = [-1, 0, 1, 0]
#         dy = [0, 1, 0, -1]
#         grid[x][y] = 0
#         for i in range(len(dx)):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == '1':
#                 self.dfs(grid, nx, ny)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         answer = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     answer += 1
#                     self.dfs(grid, i, j)
#
#         return answer


# class Solution:
#     grid: List[List[str]]
#
#     def dfs(self, x, y):
#         dx = [-1, 0, 1, 0]
#         dy = [0, 1, 0, -1]
#         self.grid[x][y] = 0
#         for i in range(len(dx)):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx >= 0 and ny >= 0 and nx < len(self.grid) and ny < len(self.grid[0]) and self.grid[nx][ny] == '1':
#                 self.dfs(nx, ny)
#
#     def numIslands(self, grid: List[List[str]]) -> int:
#         self.grid = grid
#         answer = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     answer += 1
#                     self.dfs(i, j)
#
#         return answer