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

N = int(input())

T = [ None ] * N
V = [ None ] * N
for i in range(N):
  T[i], V[i] = map(int, input().split())

last_time = T[-1]
T_count = 0
time = 0
ans = 0
for i in range(1, 101):
  # print(i, ans)
  if ans >= 1:
    ans-=1
  if i == T[T_count]:
    ans+=V[T_count]
    T_count+=1
  
  if i == last_time:
    break

print(ans)