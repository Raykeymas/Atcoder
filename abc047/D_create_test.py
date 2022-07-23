import random

N = 10**5
max_num = 10**9
nums = set()
for i in range(N):
  nums.add(str(random.randrange(0, max_num)))

with open("D_create_test.txt", "w", encoding="utf-8") as f:
  f.write(f"test_case\n")
  f.write(f"{len(nums)} 10\n")
  f.write(" ".join(nums))
