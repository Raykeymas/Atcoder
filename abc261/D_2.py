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
    if counter >= max_bonus[0] and reward <= max_bonus[2] and len(rewards) - i - 1 > max_bonus[0]:
        counter = 0
    else:
        counter += 1
        money += reward + bonuses[counter]
print(money)