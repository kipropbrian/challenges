#26 https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: list[int]) -> int:
    l = r  = 1
    while r < len(nums):
        if nums[r] > nums[r-1]:
            nums[l] = nums[r]
            l+=1
        r+=1
        
    print(nums)



removeDuplicates([1,2,2,3,3,4,4,6,7])