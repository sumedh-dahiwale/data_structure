'''
The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

'''


def reverseArray(nums):
    for x in range(0, len(nums) // 2):
        nums[x], nums[len(nums)-x-1] = nums[len(nums)-x-1], nums[x]


list1 = [1, 3, 5, 7, 9]

reverseArray(list1)

print(list1)
