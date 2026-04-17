"""
Exercise 2: Selection Sort (Ch 2)

Input:  an unsorted list of numbers, e.g. [5, 3, 6, 2, 10]
Output: a NEW list with the same numbers in ascending order, e.g. [2, 3, 5, 6, 10]

Rules:
    - Do NOT use sorted() or list.sort()
    - Implement the selection sort algorithm:
        1. Find the smallest item in the list
        2. Remove it and add it to a new "sorted" list
        3. Repeat until the original list is empty

After implementing, answer:
    - Big O time complexity: ?
    - Big O space complexity: ?
"""


def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    new_list = []
    while arr:

        smallest = arr[0]
        for i in range(len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]

        arr.remove(smallest)
        new_list.append(smallest)
    return new_list





if __name__ == "__main__":
    assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([3, 3, 3]) == [3, 3, 3]
    assert selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert selection_sort([-2, 5, 0, -7, 3]) == [-7, -2, 0, 3, 5]

    print("All tests passed!")
