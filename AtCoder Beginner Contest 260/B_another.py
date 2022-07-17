N,X,Y,Z = map(int,input().split(" "))
math_list = list(map(int,input().split(" ")))
english_list = list(map(int,input().split(" ")))
passed = []

math_index = [*range(len(math_list))]
sorted_math_index = sorted(math_index, key=lambda i:-math_list[i])
for i in range(X):
    passed.append(sorted_math_index.pop(0)+1)

english_index = [*range(len(english_list))]
sorted_english_index = sorted(english_index, key=lambda i:-english_list[i])
for i in range(Y):
    for k in sorted_english_index:
        if k+1 not in passed:
            passed.append(k+1)
            break

sum_list = []
for i in range(len(math_list)):
    sum_list.append(math_list[i]+english_list[i])
sum_index = [*range(len(sum_list))]
sorted_sum_index = sorted(sum_index, key=lambda i:-sum_list[i])
for i in range(Z):
    for k in sorted_sum_index:
        if k+1 not in passed:
            passed.append(k+1)
            break

passed = sorted(passed)
for p in passed:
    print(p)