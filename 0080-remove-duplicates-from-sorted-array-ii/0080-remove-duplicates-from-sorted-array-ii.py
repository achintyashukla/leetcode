class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max = 2
        n = len(nums)

        if n<= max:
            return n
        
        index = 1

        count = 1

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1

            if count <= max:
                nums[index] = nums[i]
                index += 1

        return index