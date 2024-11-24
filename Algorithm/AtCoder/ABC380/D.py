S = input()
Q = int(input())
K = list(map(int, input().split()))

first_length = len(S)

for i in range(Q):
  target_index = K[i]
  process_count = 0
  while True:
    
