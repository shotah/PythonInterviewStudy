class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        index_of_median = int(len(nums1)/2)
        if len(nums1) % 2 == 1:
          return nums1[index_of_median]
        return ((nums1[index_of_median -1 ] + nums1[index_of_median]) / 2)


nums1 = [1,2]
nums2 = [3,4]

print(
  Solution().findMedianSortedArrays(nums1, nums2)
)
