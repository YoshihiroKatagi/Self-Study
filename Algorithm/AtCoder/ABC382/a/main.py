## 2 values
# N, M = map(int, input().split())

## 2 lists
## input:
## A_i B_i
## 1   2
## 3   4
## 5   6
# A = [ None ] * N
# B = [ None ] * N
# for i in range(N):
#   A[i], B[i] = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

N, D = map(int, input().split())
S = input()

k_count = 0
for i in range(N):
  if S[i] == "@":
    k_count += 1

ans = N - (k_count - D)
print(ans)