# 0, 1 = x, y  2,3 = x2,y2

matrix = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(4):
    lst = list(map(int, input().split()))
    x1, y1 = lst[0], lst[1]
    x2, y2 = lst[2], lst[3]

    for i in range(x1, x2):
        for j in range(y1, y2):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                cnt += 1

print(cnt)