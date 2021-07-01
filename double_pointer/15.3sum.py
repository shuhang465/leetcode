#两边往中间夹，时间复杂度O(N2),空间复杂度O(1)
def threeSum(self, nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums):
        if i > len(nums)-1: break
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                res.add((nums[i], nums[j], nums[k]))
                #去除重复元素
                while j < k and nums[j] == nums[j+1]:
                        j += 1
                while j < k and nums[k] == nums[k-1]:
                        k -= 1
                j += 1
                k -= 1
    return map(list, res) 
#最暴利的解法是每个词都循环一遍，时间复杂度为O(n3),空间复杂度O(1)
def threesum(self, nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add((nums[i], nums[j], nums[k]))
    return map(list, res)
#选定两个值，然后用target减去这两个数即所找的数，因此可以用哈希表节省一层循环，时间复杂度O(N2),空间复杂度O(N)
def threeSum(self, nums):
    if len(nums) < 3:
        return []
    d = {}
    res = set()
    for i , v in enumerate(nums):
        d[v] = 1
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if -nums[i]-nums[j] in d:
                res.add(tuple(sorted([nums[i], nums[j],-nums[i]-nums[j])))
    return map(list, res)
 
