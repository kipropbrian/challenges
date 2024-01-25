#27 Leetcode https://leetcode.com/problems/remove-element/description/

def removeElement( nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+=1
    return k

def oremoveElement( nums: list[int], val: int) -> int:
    l = 0
    r = 0
    while r < len(nums):
        if r > l and nums[r] != val:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
        elif nums[l] == val: #found target
            r+=1
        elif nums[l] != val: #non target index
            l+=1
            r+=1
    return l

removeElement([0,1,2,2,3,0,4,2], 2)