def findMedianSortedArrays(nums1, nums2):

    def binarySearch(target, arr):
        left = 0
        right = len(arr)
        while left < right:
            mid = int((left + right) / 2)
            # print(left, mid, right)
            # input()
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left - 1

    combined_arr = []
    len1 = len(nums1)
    len2 = len(nums2)
    while len(combined_arr) <= (len1 + len2) / 2:
        if len(nums1) == 0:
            combined_arr.extend(nums2)
        elif len(nums2) == 0:
            combined_arr.extend(nums1)
        else:
            if nums1[0] < nums2[0]:
                idx = binarySearch(nums2[0], nums1)
                combined_arr.extend(nums1[:idx + 1])
                nums1 = nums1[idx + 1:]
            else:
                idx = binarySearch(nums1[0], nums2)
                combined_arr.extend(nums2[:idx + 1])
                nums2 = nums2[idx + 1:]

    # print("combined_arr: ", combined_arr)
    if (len1 + len2) % 2 == 1:
        mid_idx = int((len1 + len2) / 2)
        # print("mid_idx: ", mid_idx)
        return combined_arr[mid_idx]
    else:
        mid_idx = int((len1 + len2) / 2)
        return (combined_arr[mid_idx - 1] + combined_arr[mid_idx]) / 2


nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [2]
nums2 = [1,3]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [0,0]
nums2 = [0,0]
print(findMedianSortedArrays(nums1, nums2))