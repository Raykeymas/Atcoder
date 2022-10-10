N = int(input())
numbers = [int(input()) for _ in range(N)]
S = sum(numbers)
numbers = sorted(numbers)

for number in [0, *numbers]:
    if (S - number) % 10 != 0:
        print(S - number)
        exit(0)
print(0)
