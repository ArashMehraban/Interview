class MinStack():
   Min=float('inf')
   
   def __init__(self):
      self.Min=float('inf')
      self.stack = []

   def push(self, x):
      if x<=self.Min:
         self.stack.append(self.Min)
         self.Min = x
      self.stack.append(x)

   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.Min == t:
         self.Min = self.stack[-1]
         self.stack.pop()

   def top(self):
      return self.stack[-1]

   def getMin(self):
      return self.Min

if __name__ == "__main__":
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    print(m.getMin()) # -3
    m.pop()
    print(m.top())    # 0
    print(m.getMin()) # -2
