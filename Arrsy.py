nums = [2, 4, 1, 7, 6, 3, 8, 9, 5,]

def func(nums, left, right):
    if left >= right:
        return

    # Swap

    nums[left], nums[right] = nums[right], nums[left]

    # Recursive call

    func(nums, left + 1, right -1)

def reverse_arr(nums, left, right):
    func(nums, left, right)
    return nums

print(reverse_arr(nums, 1, 5))        
