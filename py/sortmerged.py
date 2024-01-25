def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return nums1
        
        k = 0
        for i in range(len(nums1), 0):
            print(i)

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([1,0], 1, [1], 1)