T = int(input())
for x in range(1, T + 1):
    S = input()
    nested = ""
    depth = 0
    for i in range(len(S)):
        difference = int(S[i]) - depth
        if difference >= 0:
            nested += '(' * difference + S[i]
        else:
            nested += ')' * (-difference) + S[i]
        depth += difference
    if depth > 0:
        nested += ')' * depth
    print("Case #{}: {}".format(x, nested))
