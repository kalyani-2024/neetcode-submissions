class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i] += 1
        arr=[]
        for key,value in d.items():
            arr.append([value,key])
        l=sorted(arr)
        ans=[]
        for j in range(-1,-k-1,-1):
            ans.append(l[j][1])
        return ans



        



        