N = int(input())

X=0
Y=0
for i in range(N):
  X_i, Y_i = input().split()
  X+=int(X_i)
  Y+=int(Y_i)

if X>Y:
  print("Takahashi")
elif X<Y:
  print("Aoki")
else:
  print("Draw")
