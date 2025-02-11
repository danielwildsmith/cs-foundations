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


# In-Place
def quickSort(nums: List[int]) -> List[int]:
    pivot_pos = -1
    pivot = nums[pivot_pos]

    # everything to the left is <= and everything to the right is >=
    # [6, 2, 3, 5, 4] get 4 in the right position
    # [4, 2, 3, 5, 6] 
    # [2, 4, 3, 5, 6]
    # [2, 3, 4, 5, 6]
    # how to divide and conquer iteratively

class Solution(object):
    def rotateRight(self, head, k):
        """
       :type head: Optional[ListNode]
       :type k: int
       :rtype: Optional[ListNode]
       """
       print(head)
	if not head or k == 0:
		return head


	length = 0
	cur = head
	while cur:
		length += 1
		cur = cur.next


	displacement = length % k
	if displacement == 0:
		return head
	
	cur = head
	for i in range(0, length - displacement - 1):
		cur = cur.next


	newHead = cur.next
	cur.next = None
