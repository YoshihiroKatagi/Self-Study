N = int(input())
K = list(map(int, input().split()))

total_sum = sum(K)
min_diff = float('inf')

for bit in range(1 << N):
  sum_A = 0
  sum_B = 0

  for i in range(N):
    if bit & (1 << i):
      sum_A += K[i]
    else:
      sum_B += K[i]
  
  min_diff = min(min_diff, abs(sum_A - sum_B))

sum_A = (total_sum + min_diff) // 2

print(sum_A)


# total_sum = sum(K)
# target = total_sum // 2

# dp = [False] * (target + 1)
# dp[0] = True

# for k in K:
#   for i in range(target, k - 1, -1):
#     dp[i] = dp[i] or dp[i - k]

# for i in range(target, -1, -1):
#   if dp[i]:
#     sum_A = i
#     break

# sum_B = total_sum - sum_A

# print(max(sum_A, sum_B))



# ans = 100000000000
# total_patterns = 2 ** N

# for i in range(total_patterns):
#   A_group = []
#   B_group = []

#   binary = format(i, f'0{N}b')

#   for j in range(N):
#     if binary[j] == '1':
#       A_group.append(K[j])
#     else:
#       B_group.append(K[j])

#   min_sum = max(sum(A_group), sum(B_group))
#   if min_sum < ans:
#     ans = min_sum


# print(ans)
