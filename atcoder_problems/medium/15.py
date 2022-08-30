S = input()
word = "keyence"
if S.startswith(word) or S.endswith(word):
    print("YES")
elif word in S:
    print("NO")
else:
    S, word = list(S), list(word)
    if S[0] != word[0]:
        print("NO")
    else:
        start_index = 0
        for i, s in enumerate(S):
            if s != word[i]:
                start_index = i
                break
        if "".join(S).endswith("".join(word[i:])):
            print("YES")
        else:
            print("NO")
