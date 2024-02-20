N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

A_before = 1
B_before = 1

for i in range(1,N):
  if A_before==1 and B_before==1:
    if abs(A[i]-A[i+1])>K and abs(B[i]-A[i+1])>K:
      A_before = 0
    if abs(A[i]-B[i+1])>K and abs(B[i]-B[i+1])>K:
      B_before = 0
    
  elif A_before==1:
    if abs(A[i]-A[i+1])>K:
      A_before = 0
    if abs(A[i]-B[i+1])<=K:
      B_before = 1
  
  elif B_before==1:
    if abs(B[i]-A[i+1])<=K:
      A_before = 1
    if abs(B[i]-B[i+1])>K:
      B_before = 0

  if A_before==0 and B_before==0:
    print("No")
    exit()

print("Yes")