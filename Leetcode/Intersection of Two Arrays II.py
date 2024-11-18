class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<len(nums2):
            out=nums1
            put=nums2
        else:
            out=nums2
            put=nums1
        i=0
        while i < len(out):
            if out[i] not in put:
                out.pop(i)
            else:
                put.remove(out[i])
                i+=1
        return out 