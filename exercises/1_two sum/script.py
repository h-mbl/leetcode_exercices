def twoSum(nums, target):
    for i in range(len(nums)):
        element = nums[i]
        reste = target - element
        if reste in nums:
            index = nums.index(reste)
            if i != index: return [i, index]
    return None
