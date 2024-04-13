N = int(input())
P = list(map(int, input().split()))
S = input()

dev = 998244353

# spoon = list()
# for i in range(N):
#     spoon.append(1)

ans_l = 0
ans_r = 0
ans_b = 0

first_person = P[0] - 1
first_hand = S[first_person]

if first_hand == "L" or first_hand == "?":
    print(first_hand)

    spoon = [1 for _ in range(N)]
    spoon[first_person] = 0

    cnt = 1

    for i in range(N):
        
        if i == 0:
             continue

        person = P[i] - 1
        hand = S[person]

        # print(person, hand)
        print(cnt)

        if hand == "?" and person != N-1:
            if spoon[person] == 1 and spoon[person + 1] == 1:
                spoon[person] = 0
            elif spoon[person] == 1 and spoon[person + 1] == 0:
                cnt *= 2
                spoon[person] = 0
            else:
                cnt = 0
                break
        elif hand == "?" and person == N-1:
            if spoon[person] == 1 and spoon[0] == 1:
                spoon[person] = 0
            elif spoon[person] == 1 and spoon[0] == 0:
                cnt *= 2
                spoon[person] = 0
            else:
                cnt = 0
                break
        elif hand == "L":
            if spoon[person] == 1:
                spoon[person] = 0
            else:
                cnt = 0
                break
        else:
            cnt = 0
            break

    ans_l += cnt
    ans_b += cnt


elif first_hand == "R" or first_hand == "?":

    spoon = [1 for _ in range(N)]
    spoon[first_person] = 0
    cnt = 1
    

    for i in range(N):
        if i == 0:
             continue

        person = P[i] - 1
        hand = S[person]

        # print(person, hand)
        print(cnt)

        if hand == "?" and person != N-1:
            if spoon[person] == 1 and spoon[person + 1] == 1:
                spoon[person + 1] = 0
            elif spoon[person] == 0 and spoon[person + 1] == 1:
                cnt *= 2
                spoon[person + 1] = 0
            else:
                cnt = 0
                break
        elif hand == "?" and person == N-1:
            if spoon[person] == 1 and spoon[0] == 1:
                spoon[0] = 0
            elif spoon[person] == 0 and spoon[0] == 1:
                cnt *= 2
                spoon[person] = 0
            else:
                cnt = 0
                break
        elif hand == "L":
            if spoon[person] == 1:
                spoon[person] = 0
            else:
                cnt = 0
                break
        else:
            cnt = 0
            break

    ans_r += cnt
    ans_b += cnt


if first_hand == "L":
    print(ans_l % dev) 
elif first_hand == "R":
    print(ans_r % dev)
else:
    print("both")
    print(ans_b % dev)