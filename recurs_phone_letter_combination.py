class Solution:
    def letterCombinations(self, digits: str) -> List[str]:        
        res = []
        dig2char = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'qprs',
                    '8': 'tuv',
                    '9': 'wxyz'}
        
        def combine(i,curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in dig2char[digits[i]]:
                combine(i+1, curStr +c)
                
        if digits:
            combine(0,"")
        return res
        
