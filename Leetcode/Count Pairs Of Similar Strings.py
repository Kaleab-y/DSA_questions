class Solution:
    def similarPairs(self, words: list[str]) -> int:
        masks = []
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks.append(mask)
        
        return sum(masks[i] == masks[j] for i in range(len(masks)) for j in range(i + 1, len(masks)))
