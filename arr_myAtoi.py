class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip().split(' ')
        s = '-'.join(s)
        if len(s) == 0:
            return 0
        elif len(s) == 1 and not s.isnumeric():
            return 0
        s = s + ' '
        i,beg,end =0,0,0
        while not s[i].isnumeric():
            if s[i:i+2] == '+-' or s[i:i+2] == '-+' or s[i:i+2] == '++' or s[i:i+2] == '--':
                return 0
            elif s[i] == ' ' or s[i] == '-' or s[i] == '+':
                i+=1
                beg+=1
                end+=1
            else:
                return 0
        while s[i].isnumeric() and i < len(s):
            end+=1
            i+=1
        sign = 1
        if s[beg-1] == '-':
            sign = -1
        s = s[beg:end]
        
        out =0
        for i in range(len(s)):
            out = out*10+(ord(s[i])-ord('0'))
            if sign > 0 and out >= 2147483647: # 2^31
                return 2147483647
            if sign < 0 and out > 2147483647:
                return -2147483648
                    
        if sign > 0:
            return out
        else:
            return -out
            
        
        
        
