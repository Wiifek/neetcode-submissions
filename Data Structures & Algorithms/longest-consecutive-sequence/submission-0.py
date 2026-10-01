class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        numsList = sorted(set(nums))
        maxCount,count,i = 1,1,1
        while i<len(numsList):
            if (numsList[i]-numsList[i-1]==1):
                count+=1
            else:
                maxCount = max(count,maxCount)
                count = 1
            i+=1    
            
        return max(count,maxCount)