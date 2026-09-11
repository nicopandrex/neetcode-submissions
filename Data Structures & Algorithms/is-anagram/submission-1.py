class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t= list(t)
        s.sort()
        t.sort()
        return s == t

        # seen = set()
        # if len(s) != len(t):
        #     return False
        # for char in s:
        #     seen.add(char)
        # for char in t:
        #     if char not in seen:
        #         return False
        # return True
           
        