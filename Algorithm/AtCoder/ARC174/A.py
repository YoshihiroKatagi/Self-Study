def maxSubArray(nums: list[int]) -> int:
    best = -1e9
    cur = 0
    
    for i in range(len(nums)):
        cur = max(nums[i], nums[i] + cur)
        best = max(best, cur)
    
    return best

def minSubArray(nums: list[int]) -> int:
    worst = 1e9
    cur = 0
    
    for i in range(len(nums)):
        cur = min(nums[i], nums[i] + cur)
        worst = min(worst, cur)
    
    return worst

N, C = list(map(int, input().split()))
A = list(map(int, input().split()))


sum_A = sum(A)


if C == 0:
    min_array = minSubArray(A)
    if min_array > 0:
        print(sum_A)
    else:
        print(sum_A - min_array)
elif C > 0:
    max_array = maxSubArray(A)
    if max_array < 0:
        print(sum_A)
    else:
        ans = (C-1)*max_array + sum_A
        print(ans)
elif C < 0:
    min_array = minSubArray(A)
    if min_array > 0:
        print(sum_A)
    else:
        ans = (C-1)*min_array + sum_A
        print(ans)

