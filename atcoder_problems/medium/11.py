N,M = map(int,input().split(" "))
a_list = [list(map(int,input().split(" "))) for _ in range(N)]
c_list = [list(map(int,input().split(" "))) for _ in range(M)]

for student in a_list:
    min_distance = 10**33
    min_index = 0
    for i,check_point in enumerate(c_list):
        distance = abs(check_point[0] - student[0]) + abs(check_point[1] - student[1])
        if distance < min_distance:
            min_distance = distance
            min_index = i
    print(min_index + 1)
