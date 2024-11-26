class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for item in nums:
            freq[item] = 1 + freq.get(item, 0)
        
        desc_freq = sorted(freq, key=freq.get, reverse=True)
        keys = list(desc_freq)
        print(keys) 
        top_k = []

        for i in range(0, k):
            top_k.append(keys[i])

        return top_k