class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for l in s:
                arr[ord(l)-ord('a')]+=1
            d[tuple(arr)].append(s)
        return d.values()
