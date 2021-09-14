class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sz1,sz2 = len(num1), len(num2)
        if sz1 == 0 or sz2 == 0:
            return '0'
       
        res = [0] * (sz1+sz2) #result
        n1_idx = 0
        n2_idx = 0
        for i in range(len(num1)-1,-1,-1):
            carry = 0
            n1 = ord(num1[i]) - 48 # ord('0') = 48
            n2_idx = 0
            for j in range(len(num2)-1,-1,-1):
                n2 = ord(num2[j])- 48
                Sum = n1*n2 + res[n1_idx + n2_idx] + carry
                # Carry for next iteration
                carry = Sum//10
                # Store result
                res[n1_idx + n2_idx] = Sum%10
                n2_idx+=1
            if  carry > 0:
                res[n1_idx + n2_idx] += carry
            n1_idx +=1
            
        # ignore '0's from the right
        i = len(res) - 1
        while (i >= 0 and res[i] == 0):
            i -= 1

        # If all were '0's - means either both or
        # one of num1 or num2 were '0'
        if (i == -1):
            return "0"

        # generate the result string
        s = ""
        while (i >= 0):
            s += chr(res[i] + 48)
            i -= 1

        return s
            
  
        
