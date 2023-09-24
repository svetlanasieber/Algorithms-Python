def binary_search(nums, target, left, right):
    mid_idx = (left + right) // 2
    mid_num = nums[mid_idx]

    if left > right:
        return -1       # This number doesn't exist

    if mid_num == target:
        return mid_idx

    if target < mid_num:
        right = mid_idx - 1
    else:
        left = mid_idx + 1

    return binary_search(nums, target, left, right)


nums = list(map(int, input().split()))
target = int(input())
left = 0
right = len(nums) - 1

print(binary_search(nums, target, left, right))
