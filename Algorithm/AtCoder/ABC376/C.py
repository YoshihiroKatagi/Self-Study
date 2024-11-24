N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

# print(A)
# print(B)

not_match = 0
ans = 0
a_count = 0
b_count = 0
while(a_count < N):
  if b_count == N - 1:
    ans = A[a_count]
    break
  a = A[a_count]
  b = B[b_count]
  if a <= b:
    a_count += 1
    b_count += 1
  else:
    ans = a
    not_match += 1
    a_count += 1
  
  if not_match > 1:
    print(-1)
    break


if not_match <= 1:
  print(ans)