N = int(input())

div_3_num = N // 3
div_5_num = N // 5
div_15_num = N // 15
ans = div_3_num + div_5_num - div_15_num
print(ans)