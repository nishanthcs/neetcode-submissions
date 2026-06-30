class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Matrix Representation ( Adjacency matrix)
        # Iterate through the array, and do DFS if first land if found
        # store the visited (i,j) in a set



        num_of_islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(startI, startJ):
            stack = []

            stack.append((startI,startJ))

            def add_neighbors(x,y):
                # print("XY",x,y)
                if x >=0 and x<rows and y>=0 and y<cols and (x,y) not in visited:
                    if grid[x][y] == "1":
                        stack.append((x,y))

            while stack:
                v_i,v_j = stack.pop()
                if (v_i,v_j) not in visited:
                    print(v_i,v_j)
                    visited.add((v_i,v_j))

                    # visit all neighbors
                    add_neighbors(v_i,v_j+1)
                    add_neighbors(v_i,v_j-1)
                    add_neighbors(v_i+1,v_j)
                    add_neighbors(v_i-1,v_j)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                if grid[i][j] == "1" and (i,j) in visited:
                    continue

                num_of_islands += 1

                dfs(i,j)

        return num_of_islands