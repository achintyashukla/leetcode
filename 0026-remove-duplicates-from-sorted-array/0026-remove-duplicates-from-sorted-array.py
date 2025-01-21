class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = [nums[0]]
        for n in nums[1:]:
            if n != unique[-1]:
                unique.append(n)
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)