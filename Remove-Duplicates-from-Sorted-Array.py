class Solution:
    def removeDuplicates(self, nums: List[int]):
        # counter = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[counter] = nums[i]
        #         counter += 1
        # return counter

        nums[:]=sorted(set(nums))
        return len(nums)