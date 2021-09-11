class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_r = len(board)
        num_c = len(board[0])
        word_sz = len(word)
        
        def dfs(r,c,pos):
            if pos >= word_sz:
                return True
            elif (0 <= r < num_r and 0 <= c < num_c and board[r][c] == word[pos]):
                tmp = board[r][c]
                board[r][c] = '$'
                if( dfs(r-1,c,pos+1) or
                    dfs(r+1,c,pos+1) or
                    dfs(r,c+1,pos+1) or
                    dfs(r,c-1,pos+1)):
                    return True
                board[r][c] = tmp
            return False
                  
        
        for r in range(num_r):
            for c in range(num_c):
                if dfs(r,c,0):
                    return True
        return False
        
