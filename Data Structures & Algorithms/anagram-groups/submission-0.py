class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # words = defaultdict(list)
        # for word in strs:
        #     sWord = ''.join(sorted(word)) #turns sorted word list into a str, sorted() returns a list
        #     words[sWord].append(word)
        # return list(words.values())

        # words = {}
        # for word in strs:
        #     sortedWord = ''.join(sorted(word))
        #     if sortedWord not in words.keys():
        #         words[sortedWord] = []
        #     h = words[sortedWord]
        #     h.append(word)
        # return list(words.values())  #same thing just kinda how my brain thinks of it

        #optimal solution

        result = defaultdict(list) #mapping char count of each string to list of Anagarams, makes default values a list

        for s in strs:
            count = [0] * 26 #one number place for each char, a-z

            for c in s:
                count[ord(c) - ord("a")] +=1 #substracting acii values to find placements for each letter, i a-a = 0 b-a = 1
            
            result[tuple(count)].append(s)

        return list(result.values())








    
                
        