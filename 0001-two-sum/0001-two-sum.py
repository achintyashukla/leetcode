class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in hashTable:
                return [hashTable.get(diff), i]
            
            hashTable[n] = i

        return