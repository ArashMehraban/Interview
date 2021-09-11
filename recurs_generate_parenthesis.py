class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        def rec(left,right,stack,candidate):
            if left == right == 0:
                output.append(candidate)
                return
            if left > 0:
                rec(left-1,right,stack+1,candidate+'(')
            if right > 0 and stack > 0:
                rec(left,right-1,stack-1,candidate+')')
                
        rec(n,n,0,'')
        return output
            
        
