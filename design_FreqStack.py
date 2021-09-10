from collections import Counter, defaultdict

class FreqStack:
    def __init__(self):
        self.counter = Counter()       # {4: 1, 6: 2, 7: 2, 8: 1}
        self.stack = defaultdict(list) # {1: [4,6,7,8], 2:[6,7]}
        self.maxfreq = 0               # 2

    def push(self,x):
        self.counter[x] += 1
        self.maxfreq = max(self.maxfreq,self.counter[x])
        self.stack[self.counter[x]].append(x)

    def pop(self):
        to_pop = self.stack[self.maxfreq].pop()
        self.counter[to_pop] -= 1
        if not self.stack[self.maxfreq]:
            self.maxfreq -= 1
        return to_pop

if __name__ == '__main__':
    fs = FreqStack()
    fs.push(4)
    fs.push(6)
    fs.push(7)
    fs.push(6)
    fs.push(7)
    fs.push(8)
    print(fs.pop()) # 7
    print(fs.pop()) # 6
    print(fs.pop()) # 8

