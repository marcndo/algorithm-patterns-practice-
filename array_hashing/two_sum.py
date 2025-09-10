def two_sum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
        
def two_sum_(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[nums[i]] = i




