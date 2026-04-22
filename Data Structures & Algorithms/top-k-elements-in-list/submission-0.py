class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_map = {}

        bucket = [[]for _ in range(len(nums)+1)]

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1
            
            #filling the bucket
        for key, frequency in frequency_map.items():
            bucket[frequency].append(key)

        result = []

        for i in reversed (range((len(bucket)))):
            if bucket[i]:
                for value in bucket[i]:
                    if len(result) < k:
                        result.append(value)
                    else:
                        return result
        return result

        