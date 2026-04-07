class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            print(len(s)+32)
            c = chr(len(s)+32)
            print(c)
            print(ord(c))
            res += chr(len(s)+32) + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ord(s[i]) - 32
            print(length)
            res.append(s[i+1:i+1+length])
            i += length + 1
        return res
