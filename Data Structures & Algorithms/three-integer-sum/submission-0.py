class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = set()
        l = len(nums)
        i = 0
        while i < l-2:
            left, right = i + 1, l - 1
            while left < right:
                total = sortedNums[i] + sortedNums[left] + sortedNums[right]
                if total == 0:
                    res.add((sortedNums[i], sortedNums[left], sortedNums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
        return list(res)