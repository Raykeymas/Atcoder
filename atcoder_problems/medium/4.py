S = input()

len_s = len(S)

for i in range(2,len_s,2):
    tmp_s = S[:-i]
    if tmp_s[0:round(len(tmp_s)/2)] == tmp_s[round(len(tmp_s)/2):]:
        print(len(tmp_s))
        break