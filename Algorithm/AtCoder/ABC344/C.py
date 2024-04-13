input()
A=list(map(int,input().split()))
input()
B=list(map(int,input().split()))
input()
C=list(map(int,input().split()))
S=set()
for a in A:
  for b in B:
    for c in C:
      S.add(a+b+c)
input()
X=list(map(int,input().split()))
for x in X:
  if x in S:
    print("Yes")
  else:
    print("No")