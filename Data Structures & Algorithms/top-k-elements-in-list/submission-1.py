class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_new = []
        dicts = {}
        for i in nums:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        
        dicts = dict(sorted(dicts.items(),key = lambda x:x[1], reverse = True))
        

        for key,value in dicts.items():
            nums_new.append(key)
          
            
        return nums_new[:k]
        