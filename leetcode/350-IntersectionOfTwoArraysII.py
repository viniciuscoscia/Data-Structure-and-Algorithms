from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    dic = dict()
    list_to_parse = None
    other_list = None
    result = []

    if len(nums1) < len(nums2):
        list_to_parse = nums1
        other_list = nums2
    else:
        list_to_parse = nums2
        other_list = nums1

    for item in list_to_parse:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] = dic[item] + 1

    for item in other_list:
        if item in dic and dic[item] > 0:
            dic[item] -= 1
            result.append(item)

    return result


# Claude AI below
def intersect_ai1(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Find the intersection of two arrays, including duplicates.

    Args:
        nums1: First list of integers
        nums2: Second list of integers

    Returns:
        List containing all elements that appear in both lists,
        including duplicates

    Example:
        >>> Solution().intersect([1,2,2,1], [2,2])
        [2,2]
        >>> Solution().intersect([4,9,5], [9,4,9,8,4])
        [4,9]
    """
    # Use Counter to count occurrences
    counts = Counter(nums1)
    result = []

    # Check each number in nums2
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1

    return result

def intersect_ai2(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find the intersection of two arrays, including duplicates."""
    # Get counts of both lists
    c1 = Counter(nums1)
    c2 = Counter(nums2)

    # Find common elements with minimum count
    return list((c1 & c2).elements())