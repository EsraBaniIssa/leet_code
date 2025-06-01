class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     result = {}
    #     max_times = 0
    #     max_index = -1
    #     for num in nums:
    #         if num in result.keys():
    #             result[num] += 1
    #         else:
    #             result[num] = 1
    #         if result[num] > max_times:
    #             max_times = result[num]
    #             max_index = num
    #     if max_times > len(nums)/2:
    #         return max_index
        # print(max_index, max_times)
        # return None
    # def majorityElement(self, nums: List[int]) -> int:
    #     for j in nums:
    #         cand = j
    #         cand_times = 1
    #         if len(nums)==1:
    #             return cand
    #         for i in nums[1:]:
    #             if i == cand:
    #                 cand_times +=1
    #             if cand_times >= len(nums)/2:
    #                 return cand

    # def majorityElement(self, nums: List[int]) -> int:
    #     major_element = nums[0]
    #     count = 1

    #     for i in range(1,len(nums)):
    #         if count == 0:
    #             major_element = nums[i]
    #             count = 1
    #         elif nums[i] == major_element:
    #             count += 1
    #         else:
    #             count -= 1
    #     return major_element

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
        



        