H,W = map(int,input().split(" "))
grid = [list(input()) for _ in range(H)]
all_white_row_index = set()
for h in range(H):
    result = set(grid[h])
    if len(result) == 1 and list(result)[0] == ".":
        all_white_row_index.add(h)

transpose = list(zip(*grid))
all_white_column_index = set()
for w in range(W):
    result = set(transpose[w])
    if len(result) == 1 and list(result)[0] == ".":
        all_white_column_index.add(w)

for h in range(H):
    if h not in all_white_row_index:
        output = ""
        for w in range(W):
            if w not in all_white_column_index:
                output+=grid[h][w]
        print(output)
