N, A, B = map(int, input().split())

sum_N = round(N * (N + 1) / 2)

n_a = N // A
sum_A = round(n_a * (n_a + 1) * A / 2)

n_b = N // B
sum_B = round(n_b * (n_b + 1) * B / 2)

n_ab = N // (A * B)
sum_AB = round(n_ab * (n_ab + 1) * A * B / 2)
# print(sum_N)
# print(sum_A)
# print(sum_B)
# print(sum_AB)

ans = sum_N - sum_A - sum_B + sum_AB
print(ans)