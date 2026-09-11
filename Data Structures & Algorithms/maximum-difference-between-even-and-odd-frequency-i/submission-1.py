class Solution:
    def maxDifference(self, s: str) -> int:
        chars = defaultdict(int)
        odd = []
        even = []
        for char in s:
            chars[char] +=1

        for char in chars.keys():
            if chars[char] % 2:
                odd.append(chars[char])
            else:
                even.append(chars[char])

        max_odd = max(odd)
        max_even = max(even)

        min_even = min(even)
        min_odd = min(odd)

        

        return max_odd - min_even