class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ''.join(filter(str.isalnum, s)).lower()
        if len(cleanStr)==0 or len(cleanStr)==1: return True
        l = len(cleanStr)
        start = 0
        end = l-1
        while start <= l/2:
            if cleanStr[start] != cleanStr[end]:
                return False
            start+=1
            end-=1
        return True