N = int(input())

robots = [list(map(int, input().split(" "))) for _ in range(N)]
robots = sorted(robots, key=lambda x: x[0])

right_position = robots[0][0]+robots[0][1]
remove_cnt = 0

for robot in robots[1:]:
    if robot[0]-robot[1] < right_position:
        remove_cnt += 1
        if right_position > robot[0]+robot[1]:
            right_position = robot[0]+robot[1]
    else:
        right_position = robot[0]+robot[1]

print(len(robots) - remove_cnt)
