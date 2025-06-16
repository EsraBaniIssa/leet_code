class Solution:
#     def search_rec(self,nums, target, this_index):
#         print(this_index)
#         if (len(nums[this_index:]) == 1 or len(nums[:this_index])==1):
#             if target > nums[this_index]:
#                 return this_index+1
#             if target < nums[this_index]:
#                 return this_index-1    
#         else:
#             if (target > nums[this_index] and target < nums[this_index+1]):
#                 return this_index+1
#             if (target < nums[this_index] and target > nums[this_index-1]):
#                 return this_index

#         if target > nums[this_index]:
#             this_index = this_index + len(nums[this_index:])//2
#         elif target < nums[this_index]:
#             this_index = len(nums[:this_index])//2
#         else:
#             return this_index
#         return self.search_rec(nums, target, this_index)
    # def searchInsert(self, nums: List[int], target: int) -> int:
        # if target <= nums[0]:
        #     return 0
        # if target == nums[-1]:
        #     return len(nums)-1
        # if target > nums[-1]:
        #     return len(nums)
        # return self.search_rec(nums, target, 0)
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            if target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return low

    