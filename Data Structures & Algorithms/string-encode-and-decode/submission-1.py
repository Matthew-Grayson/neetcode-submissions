class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += chr(len(s)+32) + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ord(s[i]) - 32
            res.append(s[i+1:i+1+length])
            i += length + 1
        return res
