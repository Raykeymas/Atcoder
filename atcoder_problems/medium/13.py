N = int(input())
processes = [list(map(int, input().split(" "))) for _ in range(N)]
processes.insert(0, [0, 0, 0])
for i in range(0, len(processes)-1):
    t_difference = processes[i+1][0] - processes[i][0]
    distance = abs(processes[i+1][1] - processes[i][1]) + \
        abs(processes[i+1][2] - processes[i][2])
    if t_difference < distance:
        print("No")
        exit(0)
    elif t_difference == distance:
        continue
    else:
        if (t_difference % distance) % 2 == 0:
            continue
        else:
            print("No")
            exit(0)
print("Yes")
