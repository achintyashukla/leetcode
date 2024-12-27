class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i