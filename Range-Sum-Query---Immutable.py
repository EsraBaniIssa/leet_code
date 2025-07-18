# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
        

#     def sumRange(self, left: int, right: int) -> int:
#         # result = 0
#         # for i in range(left, right+1):
#         #     result += self.nums[i]
#         # return result
#         return sum(self.nums[left:right+1])

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        # Compute prefix sums
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def sumRange(self, left: int, right: int) -> int:
        # Return difference of prefix sums
        return self.prefix[right + 1] - self.prefix[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)