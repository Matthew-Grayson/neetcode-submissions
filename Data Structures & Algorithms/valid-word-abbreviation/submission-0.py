class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j] == "0":
                return False
            
            if abbr[j].isdigit():
                subLen = 0
                while j < len(abbr) and abbr[j].isdigit():
                    subLen = subLen * 10 + int(abbr[j])
                    j += 1
                i += subLen
                
            elif word[i] != abbr[j]:
                return False
            else:
                i, j = i + 1, j + 1

        return i == len(word) and j == len(abbr)