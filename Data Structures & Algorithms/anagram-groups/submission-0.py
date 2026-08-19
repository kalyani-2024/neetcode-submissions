class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        l=[]
        for i in strs:
            key=str(sorted(i))
            if key not in group:
                group[key]=[]
            group[key].append(i)
        return list(group.values())
        