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

def count_numbers_with_9_divisors(N):
    import math

    # エラトステネスの篩で素数を列挙
    def sieve_of_eratosthenes(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [x for x in range(limit + 1) if is_prime[x]]

    count = 0

    # パターン1: p^8 の形
    max_p1 = int(N**(1 / 8))  # p^8 <= N となる最大の p
    primes = sieve_of_eratosthenes(max_p1)
    count += len(primes)  # 各 p^8 が条件を満たす

    # パターン2: p1^2 * p2^2 の形
    max_p2 = int(N**(1 / 4))  # p1^2 * p2^2 <= N となる最大の p1, p2
    primes = sieve_of_eratosthenes(max_p2)
    num_primes = len(primes)

    for i in range(num_primes):
        for j in range(i + 1, num_primes):  # p1 != p2
            if primes[i]**2 * primes[j]**2 <= N:
                count += 1
            else:
                break  # 昇順なので以降は全て条件を満たさない

    return count

# # テストケース1
# N = 200
# print(count_numbers_with_9_divisors(N))  # 出力: 3

# # テストケース2
# N = 4000000000000
# print(count_numbers_with_9_divisors(N))  # 出力: 407073


# テストケース1
# N = 200
# print(count_numbers_with_9_divisors(N))  # 出力: 3

# # テストケース2
# N = 4000000000000
# print(count_numbers_with_9_divisors(N))  # 出力: 407073

N = int(input())
print(count_numbers_with_9_divisors(N))




