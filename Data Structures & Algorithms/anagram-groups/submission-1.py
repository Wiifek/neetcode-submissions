class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            strsDict[key].append(string)
        
        return list(strsDict.values())