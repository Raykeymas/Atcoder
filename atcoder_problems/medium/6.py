H, W = map(int, input().split(" "))
bom_points = set()
maps = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
  row = list(input())
  for w in range(W):
    if row[w] == "#":
      maps[h][w] = "#"
      for dh in range(-1, 2):
        for dw in range(-1, 2):
          if h + dh < 0 or h + dh > H - 1:
            continue
          if w + dw < 0 or w + dw > W - 1:
            continue
          if maps[h + dh][w + dw] == "#":
            continue
          maps[h + dh][w + dw] += 1
for h in range(H):
  print("".join(map(str, maps[h])))
