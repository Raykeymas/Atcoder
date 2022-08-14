from collections import defaultdict
N = int(input())
numbers = list(map(int,input().split(" ")))

numbers_count = defaultdict(int)
max_count = 0
for number in numbers:
    numbers_count[number-1] += 1
    numbers_count[number] += 1
    numbers_count[number+1] += 1
    tmp_max = max(numbers_count[number-1],numbers_count[number],numbers_count[number+1])
    if max_count < tmp_max:
        max_count = tmp_max
print(max_count)
