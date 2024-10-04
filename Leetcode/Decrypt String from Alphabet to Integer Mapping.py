class Solution:
    def freqAlphabets(self, s: str) -> str:
        i, n = 0, len(s)
        res = []
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                res.append(chr(int(s[i:i+2]) + 96))
                i += 3
            else:
                res.append(chr(int(s[i]) + 96))
                i += 1
        return ''.join(res)

