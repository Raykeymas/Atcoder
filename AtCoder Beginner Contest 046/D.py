s = input()

score = [[[0]* len(s)]* len(s)]* len(s)
g = 1
p = 0
score[1][1][0] = 0

for i in range(1,len(s)):
    if s[i] == "g" and p+1 <= g:
        score[i][g][p+1] = score[i-1][g][p] + 1
        p+=1
    elif s[i] == "g" and p+1 > g:
        score[i][g+1][p] = score[i-1][g][p]
        g+=1
    elif s[i] == "p" and p+1 <= g:
        score[i][g][p+1] = score[i-1][g][p]
        p+=1
    else:
        score[i][g+1][p] = score[i-1][g][p] - 1
        g+=1
print(score[len(s)-1][g][p])

