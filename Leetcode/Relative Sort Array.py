class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        mydict = Counter(arr1)
        for i in arr2:
            out += [i] *mydict[i]
            del mydict[i]
        return out+sorted(mydict.elements())