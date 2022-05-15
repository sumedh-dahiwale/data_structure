def merge_sort(nums):
    # define the base case ( merge sort heavily relies on recursion method), split until we have just 1 element
    # arrays with single item is sorted by default

    if len(nums) == 1:  # base method
        return

    # DIVIDE PHASE
    middle_index = len(nums) // 2
    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    # CONQUER PHASE
    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            nums[k] = left_half[i]
            i += 1
        else:
            nums[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1


list1 = [2, 5, 7, 2, 9, 0]

merge_sort(list1)

print(list1)
