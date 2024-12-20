from typing import List

def mergeSort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    
    # Divide into halves
    middle = len(nums) // 2
    left = mergeSort(nums[:middle])
    right = mergeSort(nums[middle:])

    return sortTwoLists(left, right)

# Merge Sort Helper
def sortTwoLists(nums1: List[int], nums2: List[int]) -> List[int]:
    if not nums1 and not nums2:
        return []
    if not nums1:
        return nums2
    if not nums2:
        return nums1
    
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    
    if i < len(nums1):
        res.extend(nums1[i:])
    if j < len(nums2):
        res.extend(nums2[j:])
    
    return res

unsorted_arr = [5, 2, 4, 1]
print(mergeSort(unsorted_arr))