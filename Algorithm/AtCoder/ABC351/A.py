A = list(map(int, input().split()))
B = list(map(int, input().split()))

score_a = sum(A)
score_b = sum(B)

diff = score_a - score_b
ans = diff + 1
print(ans)