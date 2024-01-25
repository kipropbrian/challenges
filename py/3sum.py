# 15 https://leetcode.com/problems/3sum/description/
def threeSum(nums: list[int]) -> list[list[int]]:
    row = set()
    nums.sort()

    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        while(l < r):
            sum =  nums[i] + nums[l] + nums[r]
            if sum == 0:
               row.add((nums[i], nums[l], nums[r]))
               l+=1
               r-=1
            elif sum > 0:
                l +=1
            else:
                r -=1
    print(row)
    return row

threeSum([-1, 0, 1, 2, -1, -4])
# threeSum([1, 2, 3, 4, 5, 6])
# threeSum([0,0,0])

# def threeSum(nums: list[int]) -> list[list[int]]:
#     hash = {}
#     row = []
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if i != j :
#                 balance = 0 - (nums[i] + nums[j])
#                 if balance in hash:
#                     row.append( [*hash[balance], nums[j]] )
                
#                 hash[nums[i] + nums[j]] = [nums[i], nums[j]]
    
#     print(row)

#     return nums


# def threeSum(nums: list[int]) -> list[list[int]]:
#     row = set()
#     nums.sort()

#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#            for k in range (j+1, len(nums)):
#                 if (nums[i] + nums[j] + nums[k]) == 0: 
#                     row.add((nums[i], nums[j], nums[k]))
    
#     res = [list(t) for t in row]
#     return res

# threeSum([-1, 0, 1, 2, -1, -4])