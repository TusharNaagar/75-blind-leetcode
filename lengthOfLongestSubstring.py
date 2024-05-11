class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        l=0
        longest=0

        for r in range(len(s)):
            while s[r] in sett: 
                # If Duplicate found then remove l 
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            longest=max(longest, r-l+1)
        return longest
