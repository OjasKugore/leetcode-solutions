from math import factorial


class Solution:

  def permute(self, nums: list[int]) -> list[list[int]]:
    ans = []
    n = len(nums)
    nums.sort()

    for _ in range(factorial(n)):
      ans.append(nums.copy())

      pivot = -1
      for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
          pivot = i
          break

      if pivot != -1:
        for j in range(n - 1, pivot, -1):
          if nums[j] > nums[pivot]:
            nums[j], nums[pivot] = nums[pivot], nums[j]
            break

      left, right = pivot + 1, n - 1
      while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return ans
