T = int(input())
for x in range(1, T + 1):
    N = int(input())
    activities = [list(map(int, input().split())) + [_] for _ in range(N)]
    impossible = False
    schedule = [0] * N
    cameronsLast = jamiesLast = -1
    for start, end, i in sorted(activities):
        if impossible:
            break
        if start < cameronsLast:
            if start < jamiesLast:
                impossible = True
                break
            else:
                jamiesLast = max(jamiesLast, end)
                schedule[i] = 'J'
        else:
            cameronsLast = max(cameronsLast, end)
            schedule[i]= 'C'
    res = ''
    if impossible:
        res = "IMPOSSIBLE"
    else:
        res = ''.join(schedule)
    print("Case #{}: {}".format(x, res))
