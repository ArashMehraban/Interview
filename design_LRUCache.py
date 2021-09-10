from collections import deque

class LRUcache():
    def __init__(self, cache_sz = 5):
        self.cache_sz = cache_sz
        self.dq = deque() # used as a doubly-linked-list (O(1) insertion/removal)
        self.dqmap = {} # (O(1) search)

    def put(self,val):
        if val not in self.dqmap:
            self.dqmap[val] = val
            self.dq.append(val)
            if len(self.dq) > self.cache_sz:
                self.dqmap.pop(self.dq.popleft()) # pop LRU from dq and then dqmap

    def get(self,val):
        if val in self.dqmap:
            return True
        else:
            return False

    def show(self):
        print('cache size    : ',self.cache_sz)
        print('current cache : ',self.dq)
        print('current map   : ',self.dqmap)

if __name__ == "__main__":
    lru = LRUcache(3)
    lru.show()
    # cache size    :  3
    # current cache :  deque([])
    # current map   :  {}
    print('-------------------------------------')
    lru.put(10)
    lru.put(280)
    lru.put(13)
    lru.put(4)
    lru.put(11)
    lru.show()
    # cache size    :  3
    # current cache :  deque([13, 4, 11])
    # current map   :  {13: 13, 4: 4, 11: 11}
    print(lru.get(11))  #True 
    print(lru.get(280)) #False
