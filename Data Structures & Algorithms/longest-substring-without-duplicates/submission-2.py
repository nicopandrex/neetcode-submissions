class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        longest = 0
        for right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
            else:
                while s[right] in window:
                    window.remove(s[l])
                    l+=1
                window.add(s[right])
            longest = max(longest, len(window))

                
        return longest

        