class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # board is a matrix
        # Go through each i,j in the board until you find the first letter. 
        # If you find the first letter, starting that, perform a bfs 
        # specifically looking for all letters of the word,
        # if breakage, then return
        # O(k)
        word_list = list(word)
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(x,y,c):
            if c == len(word):
                return True
            
            if x < 0 or x >= rows or y < 0 or y >=cols or board[x][y] != word[c] or (x,y) in visited:
                return False
            
            # visit 
            visited.add((x,y))
            found = dfs(x+1, y, c+1) or dfs(x-1,y,c+1) or dfs(x,y+1,c+1) or dfs(x,y-1,c+1)
            # backtrack
            visited.remove((x,y))

            return found


        for i in range(rows):
            for j in range(cols):
                found = dfs(i,j,0)

                if found:
                    return True
        
        return False
        

                    