class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_new = []
        dict = defaultdict()
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for key,value in dict.items():
            if value >= k:
                nums_new.append(key)
        return nums_new
        