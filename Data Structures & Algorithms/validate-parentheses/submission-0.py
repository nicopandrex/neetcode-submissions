class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {")":"(","]":"[","}":"{"}
        for item in s:
            if item in closeOpen.keys():
                if stack != [] and stack[-1] == closeOpen[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return not stack





        # while "()" in s or "{}" in s or "[]" in s:
        #     s = s.replace('()','')
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        # return s == ""




        # lp = 0
        # rp = 0
        # lb = 0
        # rb = 0
        # lc = 0
        # rc = 0 
        # for item in s:
        #     if "(":
        #         lp+=1
        #     if ")":
        #         rp+=1
        #     if "[":
        #         lb+=1
        #     if "]":
        #         rb+=1
        #     if "{":
        #         lc +=1
        #     if "}":
        #         rc +=1
        # return lp == rp and lb == lb and lc == rc
        