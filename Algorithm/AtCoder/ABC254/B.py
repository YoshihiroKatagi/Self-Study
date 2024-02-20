N = int(input())

def makeSequence(n):
  if n == 1:
    # if not new_A in A:
    #   A.append(new_A)
    # print(A)
    print(1)
    return new_A
  elif n == 2:
    new_A = [1, 1]
    # if not [1] in A:
    #   A.append([1])
    # new_A.append(1)
    # if not new_A in A:
    #   A.append(new_A)
    # print(A)
    print("1")
    print("1 1")
    return new_A
  else:
    new_A = [1]
    get_list = makeSequence(n-1)
    for j in range(len(get_list) - 1):
      new_num = get_list[j] + get_list[j + 1]
      new_A.append(new_num)
    new_A.append(1)
    print(new_A)
    # if not new_A in A:
    #   A.append(new_A)
    # print(A)
    # if len(A) == n:
    #   return A
    return new_A

ans_list = []
makeSequence(N)

