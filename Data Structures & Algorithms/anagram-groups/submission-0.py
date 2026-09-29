class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            strsDict[key].append(string)
        result =[]
        for array in strsDict.values():
            result.append(array)
        return result