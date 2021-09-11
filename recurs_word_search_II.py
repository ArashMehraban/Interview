#------Works and accepted but horrible style. Fix later-------------------------------------
class Solution:
    class TreeNode(object):
        def __init__(self):
            self.is_word = False
            self.children = {}
            self.ct = 0
    
    def buildTrie(self, word):
        p = self.root

        for w in word:
            if w not in p.children:
                p.children[w] = self.TreeNode()
            p = p.children[w]
            p.ct += 1
        p.is_word = True
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0:
            return []
        
        self.root = self.TreeNode()
        
        for word in words:
            self.buildTrie(word)
        
        self.res = set()
        self.direcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, '', self.root, board, set())
        
        return list(self.res)
        
    def dfs(self, i, j, cur, p, board, visited):
        if (i < 0) or (j < 0) or (i >= len(board)) or (j >= len(board[0])) or ((i, j) in visited) or (board[i][j] not in p.children) or (p.children[board[i][j]].ct == 0):
            return
        
        w = board[i][j]
        p = p.children[w]
        if p.is_word:
            self.res.add(cur+w)
            self.remove(cur+w)
            p.is_word = False
        
        visited.add((i, j))
        for direc in self.direcs:
            x = i + direc[0]
            y = j + direc[1]
            self.dfs(x, y, cur+w, p, board, visited)
        visited.remove((i, j))
    
	# !!! key points to solve TLE
	# disable the path if all the words including the char searched.
    def remove(self, word):
        p = self.root
        for w in word:
            p = p.children[w]
            p.ct -= 1
    

##  ------SLOW--------------------
##
##class Trie:
##    def __init__(self):
##        self.child = {}
##    
##    def insert(self, word):
##        cur = self.child
##        for l in word:
##            if l not in cur:
##                cur[l] = {}
##            cur = cur[l]
##        cur['#'] = True #end of word in Trie
##        
##    def search(self, word):
##        cur = self.child
##        for l in word:
##            if l not in cur:
##                return False
##            cur = cur[l]
##        return '#' in cur
##    
##    def starts_with(self, prefix):
##        cur = self.child
##        for l in prefix:
##            if l not in cur:
##                return False
##            cur = cur[l]
##        return True
##    
##
##class Solution:
##    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
##        trie = Trie()
##        for w in words:
##            trie.insert(w)
##            
##        max_r = len(board)
##        max_c = len(board[0])
##        output = []
##        
##        def dfs(row, col, path):
##            #out of bound and visited checks:
##            if (row < 0 or row >= max_r or
##                col < 0 or col>= max_c or board[row][col] == 0):
##                return
##            tmp_path = path+[board[row][col]]
##            string = ''.join(tmp_path)
##            if not trie.starts_with(string):
##                return
##            elif trie.search(string) and string not in output:
##                output.append(string)
##            placeholder = board[row][col]
##            board[row][col] = 0
##            dfs(row-1,col,tmp_path)
##            dfs(row+1,col,tmp_path)
##            dfs(row,col-1,tmp_path)
##            dfs(row,col+1,tmp_path)
##            board[row][col] = placeholder
##            
##        for r in range(max_r):
##            for c in range(max_c):
##                dfs(r,c,[])
##                
##        return output
