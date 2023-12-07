def min_max(array, start, end):
    if start == end:
        return (array[start], array[end])
    elif end - start == 1:
        min_num = min(array[start], array[end])
        max_num = max(array[start], array[end])
        return (min_num, max_num)
    else:
        mid = (start + end) // 2
        min_num1, max_num1 = min_max(array, start, mid)
        min_num2, max_num2 = min_max(array, mid+1, end)
        return (min(min_num1, min_num2), max(max_num1, max_num2))

# main
#nums = [11, -24, 0, 5, 8, 999, 123, 75, 66]

nums = [23, -20, 0, 5, -29, 45]
start = 0
end = len(nums) - 1
min_num, max_num = min_max(nums, start, end)
print("minimum is", min_num)
print("maximum is", max_num)
