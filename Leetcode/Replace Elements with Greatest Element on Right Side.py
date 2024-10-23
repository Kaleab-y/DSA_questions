class Solution:
  def replaceElements(self, arr: list[int]) -> list[int]:
    mx_right = -1
    for i in reversed(range(len(arr))):
      arr[i], mx_right = mx_right, max(mx_right, arr[i])
    return arr