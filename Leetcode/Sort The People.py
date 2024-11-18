class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        for i in range(len(heights)):
            min_cur = i
            for j in range(i+1,len(heights)):
                if heights[j] > heights[min_cur]:
                    min_cur = j
            heights[i],heights[min_cur] = heights[min_cur],heights[i]
            names[i],names[min_cur] = names[min_cur],names[i]
        return names