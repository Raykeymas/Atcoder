import copy
import math
N,X,Y,Z = map(int,input().split(" "))
math_list = list(map(int,input().split(" ")))
english_list = list(map(int,input().split(" ")))

math_list = copy.copy(math_list)
english_list = copy.copy(english_list)

passed = []
sorted_math_list = sorted(math_list,reverse=True)
for i in range(X):
    before = len(passed)
    for j in range(len(sorted_math_list)):
        max = sorted_math_list.pop(0)
        for k in range(len(math_list)):
            if max == math_list[k] and k+1 not in passed:
                passed.append(k+1)
                break
        if before != len(passed):
            break

sorted_english_list = sorted(english_list,reverse=True)
for i in range(Y):
    before = len(passed)
    for j in range(len(sorted_english_list)):
        max = sorted_english_list.pop(0)
        for k in range(len(english_list)):
            if max == english_list[k] and k+1 not in passed:
                passed.append(k+1)
                break
        if before != len(passed):
            break

sum_list = []
for i in range(len(math_list)):
    sum_list.append(math_list[i]+english_list[i])
sorted_sum_list = sorted(sum_list,reverse=True)
for i in range(Z):
    before = len(passed)
    for j in range(len(sorted_sum_list)):
        max = sorted_sum_list.pop(0)
        for k in range(len(sum_list)):
            if max == sum_list[k] and k+1 not in passed:
                passed.append(k+1)
                break
        if before != len(passed):
            break

passed = sorted(passed)
for p in passed:
    print(p)