MOD = 998244353

N = int(input())
Ps = list(map(int, input().split()))
for i in range(N):
    Ps[i] -= 1
S = input()

answer_left = 1
answer_right = 1
took_spoon = [False] * N
for P in Ps:
    if took_spoon[(P + 1) % N]:
        if S[P] == "?":
            answer_left *= 2
    else:
        if S[P] == "R":
            answer_left *= 0
    answer_left %= MOD
    if took_spoon[(P - 1) % N]:
        if S[P] == "?":
            answer_right *= 2
    else:
        if S[P] == "L":
            answer_right *= 0
    answer_right %= MOD
    took_spoon[P] = True

print((answer_left + answer_right) % MOD)