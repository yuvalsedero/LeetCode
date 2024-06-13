def merge(nums1, m, nums2, n):
    # if (m-n) < 0:
    #     nums1 = nums1
    # else:
    nums1 = nums1[m-n:n]
    for i in nums2:
        if i == 0:
            continue
        else:
            nums1.append(i)
    nums1.sort()
    print(nums1)
merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
merge(nums1 = [1], m = 1, nums2 = [], n = 0)
merge(nums1 = [0], m = 0, nums2 = [1], n = 1)