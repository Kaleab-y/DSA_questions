class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        for index in range(len(strings[0])):
            for string in strings[1:]:
                if index >= len(string) or string[index] != strings[0][index]:
                    return strings[0][:index]
        return strings[0]