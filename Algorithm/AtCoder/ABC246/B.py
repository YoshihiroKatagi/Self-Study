A, B = map(int, input().split())

import math
AB = math.sqrt(A*A + B*B)

x = 1 * A/AB
y = 1 * B/AB

print(x, y)