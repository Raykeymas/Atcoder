H, W = map(int, input().split())
cells = [list(input()) for _ in range(H)]
for i in range(len(cells)):
    for k in range(len(cells[i])):
        if cells[i][k] == "#":
            if k-1 >= 0 and cells[i][k-1] == "#":
                continue
            elif k+1 < W and cells[i][k+1] == "#":
                continue
            elif i-1 >= 0 and cells[i-1][k] == "#":
                continue
            elif i+1 < H and cells[i+1][k] == "#":
                continue
            else:
                print("No")
                exit(0)
print("Yes")
