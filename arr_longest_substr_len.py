class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		start = -1   # start index of current substring
		longest = 0  # length of the longest substring
		hash_map = dict() # hash map is to store the latest index of char

		for i in range(len(s)):
			if s[i] in hash_map and start < hash_map[s[i]]:
                            start = hash_map[s[i]] 
			hash_map[s[i]] = i 
			if i - start > longest:
                            longest = i - start 

		return longest
