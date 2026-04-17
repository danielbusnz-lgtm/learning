"""
Exercise 1: Binary Search (Ch 1)

Write binary_search(arr, target) that returns the index of `target` in a
sorted list, or None if not found.

After implementing, answer:
    - Big O time complexity: ?
    - Big O space complexity: ?
"""


def binary_search(arr, target):
    if arr == []:
        return None

    middle = len(arr) // 2
    slider = arr[middle]

    if target == slider:
        return middle

    if target < slider:
        return binary_search(arr[:middle], target)

    if target > slider:
        result = binary_search(arr[middle + 1:], target)
        if result is None:
            return None
        return middle + 1 + result


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 19) == 9
    assert binary_search(nums, 11) == 5
    assert binary_search(nums, 4) is None
    assert binary_search([], 3) is None
    assert binary_search([42], 42) == 0
    assert binary_search([42], 7) is None

    print("All tests passed!")
