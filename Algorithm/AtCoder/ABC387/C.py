# def is_snake_number(n):
#     digits = list(map(int, str(n)))
#     first_digit = digits[0]
#     for d in digits[1:]:
#         if d >= first_digit:
#             return False
#     return True

# def count_snake_numbers_up_to(X):
#     count = 0
#     for num in range(1, X + 1):
#         if is_snake_number(num):
#             count += 1
#     return count

# def count_snake_numbers(L, R):
#     return count_snake_numbers_up_to(R) - count_snake_numbers_up_to(L - 1)

# # 入力
# L, R = map(int, input().split())

# # 出力
# print(count_snake_numbers(L, R))


def is_snake_number(n):
    digits = list(map(int, str(n)))
    first_digit = digits[0]
    for d in digits[1:]:
        if d >= first_digit:
            return False
    return True

def count_snake_numbers_up_to(X):
    # Xまでの範囲でヘビ数の個数を動的計算
    count = 0
    for num in range(1, X + 1):
        if is_snake_number(num):
            count += 1
    return count

def count_snake_numbers(L, R):
    return count_snake_numbers_up_to(R) - count_snake_numbers_up_to(L - 1)

# 入力
L, R = map(int, input().split())

# 出力
print(count_snake_numbers(L, R))
