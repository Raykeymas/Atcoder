from collections import defaultdict
import bisect
N, K = map(int, input().split(" "))
p_list = list(map(int, input().split(" ")))

all_cards = []
field_cards = []
append = field_cards.append
ans = defaultdict(lambda: -1)

if K == 1:
  for i in range(N):
    ans[p_list[i]] = i + 1
else:
  for i, num in enumerate(p_list):
    index = bisect.bisect(all_cards, num)
    if index == len(all_cards):
      all_cards.append(num)
      field_cards.append([num])
    else:
      all_cards[index] = num
      field_cards[index].append(num)
    if len(field_cards[index]) == K:
      for card in field_cards[index]:
        ans[card] = i + 1
      all_cards.pop(index)
      field_cards.pop(index)

for i in range(N):
  print(ans[i + 1])
