from collections import defaultdict

N, M = map(int,input().split(" "))
rewards = list(map(int,input().split(" ")))
bonuses = defaultdict(int)
max_bonus = [0,0,0]
for i in range(M):
    c,y = map(int,input().split(" "))
    bonuses[c] = y
    if max_bonus[2] < y/c:
        max_bonus = [c,y,y/c]

counter = 0
money = 0
for i,reward in enumerate(rewards):
    if counter >= max_bonus[0] and len(rewards) - i - 1 > max_bonus[0]:
        false_sum = 0
        for j in range(1,max_bonus[0]+1):
            false_sum += rewards[i+j]
        false_sum += max_bonus[1]
        true_sum = reward
        for j in range(2,max_bonus[0]+1):
            true_sum += rewards[i+j]
        if true_sum > false_sum:
            counter += 1
            money += reward + bonuses[counter]
        else:
            counter = 0
    else:
        counter += 1
        money += reward + bonuses[counter]
print(money)