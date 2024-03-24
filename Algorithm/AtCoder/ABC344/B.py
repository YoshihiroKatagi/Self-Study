# A = list()
# for i in range(100):
#     a = input()
#     A.append(a)

# for i in range(len(A)):
#     print(A[-(i+1)])

lines = input_lines.split('\n')

if lines[-1] == '':
    lines.pop()

for line in lines:
    print(line)