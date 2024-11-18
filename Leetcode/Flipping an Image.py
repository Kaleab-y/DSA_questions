class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        size = len(image)
        for i in range(size):
            row = image[i][::-1]
            row = list(map(lambda pxl: 0 if pxl == 1 else 1, row))
            image[i] = row
        return image
        