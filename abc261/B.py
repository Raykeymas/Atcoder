from collections import defaultdict

N =int(input())
results = []
for i in range(N):
    result = list(input())
    results.append(result)
def judge(a,b):
    if a == "W" and b == "L":
        return True
    elif a == "L" and b == "W":
        return True
    elif a == "D" and b == "D":
        return True
    else:
        return False

already_judge = defaultdict(int)

for i,result in enumerate(results):
    for j,r in enumerate(result):
          if i != j and already_judge[(i,j)] == 0:
                if not judge(r,results[j][i]):
                    print("incorrect")
                    exit(0)
                else:
                    already_judge[(i,j)] = 1
print("correct")