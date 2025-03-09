t = int(input())
for _ in range(1, t+1):
    lst = list(map(int, input().split()))
    tc = lst[0]
    hs = lst[1:]

    line = []
    cnt = 0

    for h in hs:
        