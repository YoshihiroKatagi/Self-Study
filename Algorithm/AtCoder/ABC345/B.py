x = int(input())

a_float = x / 10
a_int = x // 10

print(a_float)
print(a_int)
if a_float > a_int:
    print(a_int + 1)
elif a_float < 0:
    print(a_int)
elif a_float == a_int:
    print(a_int)
