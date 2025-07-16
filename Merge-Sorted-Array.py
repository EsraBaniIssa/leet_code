class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if len(nums2) == 0 or n ==0:
        #     return
        # if len(nums1) ==0 or m ==0:
        #     for i in range(len(nums2)):
        #         nums1[i] = nums2[i]
        #     # nums1 = [i for i in range(len(nums2))]
        #     return
        # index_nums1 = m-1
        # index_nums2 = n-1
        # for i in range(m+n-1, 0, -1):
        #     if (nums2[index_nums2]>= nums1[index_nums1] and index_nums2>=0) or index_nums1<0:
        #         nums1[i] = nums2[index_nums2]
        #         index_nums2 = index_nums2 - 1
        #     else:
        #         nums1[i] = nums1[index_nums1]
        #         index_nums1 = index_nums1 - 1

        index_nums1 = m-1
        index_nums2 = n-1
        main_index = m+n-1

        while index_nums1 >= 0 and index_nums2 >= 0:
            if nums2[index_nums2] > nums1[index_nums1]:
                nums1[main_index] = nums2[index_nums2]
                index_nums2 -= 1
            else:
                nums1[main_index] = nums1[index_nums1]
                index_nums1 -= 1
            main_index -= 1

        while index_nums2 >= 0:
            nums1[main_index] = nums2[index_nums2]
            main_index -= 1
            index_nums2 -= 1
