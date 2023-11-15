def twoSum(nums: list[int], target: int) -> list[int]:
    remainderList = {}

    for key, current in enumerate(nums):
        if current in remainderList:
            return [remainderList[current], key]
        remainder = target - current
        remainderList[remainder] = key


assert(twoSum([2, 7, 11, 15], 9) == [0, 1])
assert(twoSum([3,2,4], 6) == [1, 2])
assert(twoSum([3,3], 6) == [0, 1])
assert(twoSum([2,3,4,5,6,7,8,9,0,12,13,99,77,56], 58) == [0, 13])
assert(twoSum([2,3,4,15,22,7,8,9,0,12,13,99,77,56], 133) == [12, 13])
twoSum()

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            print('-------')
            for j in range(i+1, len(nums)):
                print(nums[i], nums[j])


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for k,v in enumerate(nums):
            print('-------')
            for ke, va in enumerate(nums[k+1:]):
                print(v, va)
                if ke != k:
                    if v + va == target:
                        return [k, ke]


test = Solution()
twoSum([2,7,11,15], 9)
test.twoSum([3,2,4], 6)
test.twoSum([3,3], 6)
