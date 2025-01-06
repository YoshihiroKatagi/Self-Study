import copy

class round:
  def __init__(self, p, q, r):
    self.p = p
    self.q = q
    self.r = r

class state:
  def __init__(self, n):
    self.score = 0
    self.x = [ 0 ] * n
    self.lastmove = '?'
    self.lastpos = -1

def beam_search(N, T, rounds):
  WIDTH = 10000
  beam = [ list() for i in range(T + 1) ]
  beam[0].append(state(N))

  for i in range(T):
    candidate = list()
    for j in range(len(beam[i])):
      sousa_a = copy.deepcopy(beam[i][j])
      sousa_a.lastmove = 'A'
      sousa_a.lastpos = j
      sousa_a.x[rounds[i].p] += 1
      sousa_a.x[rounds[i].q] += 1
      sousa_a.x[rounds[i].r] += 1
      sousa_a.score += sousa_a.x.count(0)

      sousa_b = copy.deepcopy(beam[i][j])
      sousa_b.lastmove = lastmove = 'B'
      sousa_b.lastpos = j
      sousa_b.x[rounds[i].p] -= 1
      sousa_b.x[rounds[i].q] -= 1
      sousa_b.x[rounds[i].r] -= 1
      sousa_b.score += sousa_b.x.count(0)

      candidate.append(sousa_a)
      candidate.append(sousa_b)
    
    candidate.sort(key = lambda s: -s.score)
    beam[i + 1] = copy.deepcopy(candidate[:WIDTH])
  
  current_place = 0
  answer = [ None ] * T
  for i in range(T, 0, -1):
    answer[i - 1] = beam[i][current_place].lastmove
    current_place = beam[i][current_place].lastpos
  return answer

T = int(input())
rounds = [ None ] * T
for i in range(T):
  p, q, r = map(int, input().split())
  rounds[i] = round(p - 1, q - 1, r - 1)

answer = beam_search(20, T, rounds)

for c in answer:
  print(c)