class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            Aleft = float("-inf") if i == 0 else nums1[i - 1]
            Aright = float("inf") if i == m else nums1[i]

            Bleft = float("-inf") if j == 0 else nums2[j - 1]
            Bright = float("inf") if j == n else nums2[j]

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1