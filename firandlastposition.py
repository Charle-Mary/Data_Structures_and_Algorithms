def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    N = len(nums)
    l, r = 0, N - 1
    st, end = -1, -1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1

    if l < N and nums[l] == target:
        st = l

    l, r = 0, N - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1

    if nums[r] == target:
        end = r

    return [st, end]


print(searchRange([5,6,7,7,8,8,10], 10))