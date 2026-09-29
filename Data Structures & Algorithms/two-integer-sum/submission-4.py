class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {num: index for index,num in enumerate(nums)}
        for index,num in enumerate(nums):
            num2 = target-num
            if num2 in numsDict:
                num2Index = numsDict.get(num2)
                if num2Index != index:
                    return [index,num2Index]
        return []
                
        