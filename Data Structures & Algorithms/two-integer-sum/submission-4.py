class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # assume only one answer
        indexed = sorted((val, i) for i, val in enumerate(nums))
        pointer1 = 0
        pointer2 = len(nums) -1
        while pointer1 < pointer2:
            sums = indexed[pointer1][0] + indexed[pointer2][0]
            if sums > target:
                pointer2 -= 1
            elif sums < target:
                pointer1 += 1
            else: 
                idx1 = indexed[pointer1][1]
                idx2 = indexed[pointer2][1]
                return [min(idx1, idx2), max(idx1, idx2) ]

