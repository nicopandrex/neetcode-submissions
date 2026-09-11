class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for word in s.split():
            
            count = len(word)
        return count