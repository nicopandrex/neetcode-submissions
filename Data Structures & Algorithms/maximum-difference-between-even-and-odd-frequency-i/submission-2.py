class Solution:
    def maxDifference(self, s: str) -> int:
        chars = defaultdict(int)
        max_odd = float("-inf")
        min_even = float("inf")
        for char in s:
            chars[char] +=1

        for char in chars.keys():
            if chars[char] % 2:
               max_odd = max(max_odd, chars[char])
            else:
                min_even = min(min_even, chars[char])
        return max_odd - min_even

    
