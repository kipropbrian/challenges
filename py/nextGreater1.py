def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    # create a new array of length nums1
    results = [-1] * len(nums1)

    # map nums1 to its index
    nums1dict = {}
    for i, num in enumerate(nums1):
        nums1dict[num] = i

    next = 0
    for j, num in enumerate(nums2):
        if num in nums1dict:
            for k in range(j + 1, len(nums2)):
                if nums2[k] > num:
                    results[nums1dict[num]] = nums2[k]
                    break

            next = j + 1
            while next < len(nums2):
                if nums2[next] > num:
                    results[nums1dict[num]] = nums2[next]
                    break
                else:
                    next += 1
    print(results)
    return results


nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
nextGreaterElement([4, 1, 2], [1, 3, 4, 2, 7, 99, -1, 444])
nextGreaterElement([4, 1, 2], [1, 3, 4, 2, 7, 99, -1, 444])


def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    greaterElementMap = {}
    results = []
    main = 0
    next = 1

    while main < len(nums2):
        if next >= len(nums2):
            greaterElementMap[nums2[main]] = -1
            main += 1
            next = main + 1
        elif nums2[next] > nums2[main]:
            greaterElementMap[nums2[main]] = nums2[next]
            main += 1
        else:
            next += 1
    for num in nums1:
        results.append(greaterElementMap[num])
    print(results)
    return results


# nextGreaterElement([2,4], [1,2,3,4])
# {"1": -1, "3": -1}
