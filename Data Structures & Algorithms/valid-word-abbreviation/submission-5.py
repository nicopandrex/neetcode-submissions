class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word)  and j < len(abbr):
            if word[i] == abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isdigit() and int(abbr[j]) != 0:
                print(abbr[j])
                num = ""
                while j < len(abbr) and abbr[j].isdigit():
                    num += str(abbr[j])
                    j+=1
                i+= int(num)
                
            else:
                return False
        return i == len(word) and j == len(abbr)
