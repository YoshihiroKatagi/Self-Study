def get_diff_array(A, l, r, value):
  A[l] += value
  if r < len(A):
    A[r] -= value

N = int(input())
A = list(map(int, input().split()))

distributed_stones = [0] * (N + 1)
answer = [ None ] * N

for i in range(N):
  if i > 0:
    distributed_stones[i] += distributed_stones[i - 1]

  distributed_stone = distributed_stones[i]
  first_stone = A[i]
  total_stones = distributed_stone + first_stone
  expect_to_distribute = N - (i + 1)
  distribute_count = min(total_stones, expect_to_distribute)

  # print("==== check ====")
  # print("i: ", i)
  # print("distributed_stone: ", distributed_stone)
  # print("first_stone: ", first_stone)
  # print("total_stones: ", total_stones)
  # print("expect_to_distribute: ", expect_to_distribute)
  # print("distribute_count: ", distribute_count)
  # print("==== check ====\n")

  if distribute_count > 0:
    get_diff_array(distributed_stones, i + 1, i + 1 + distribute_count, 1)
  
  answer[i] = total_stones - distribute_count

print(" ".join(map(str, answer)))