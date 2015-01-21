'''
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''

# recursion but too slow for large strings doesn't stop on max number
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
		def recur(s):
			if len(s) == len(set(s)):
				return s
			else:
				a = recur(s[1:])
				b = recur(s[:-1])
				if len(a) > len(b):
					return a
				else: 
					return b
					
		r = recur(s)
		return len(r)

# quicker but still didn't pass the test		
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
		bag = set()
		bag.add(s)
		for i in range(len(s)):
			for b in list(bag):
				if len(b) == len(set(b)):
					return len(b)
				bag.add(b[1:])
				bag.add(b[:-1])
				bag.remove(b)
		return 0
		
