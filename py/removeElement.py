#27 Leetcode https://leetcode.com/problems/remove-element/description/

def removeElement( nums: list[int], val: int) -> int:
    l = 0
    for r in range(len(nums)):
        if r == 2:
            r += 10
        print("After:", r)
       

    # for r in range(len(nums)):
    #     print(l, r)
    #     print(nums[r])
    #     if nums[r] == val:
    #         r += 1
    #     else:
    #         l +=1


removeElement([1,2,3,4,5], 3)