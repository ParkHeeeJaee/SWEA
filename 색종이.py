matrix = [[0] * 100 for _ in range(100)]
# 색종이의 수
n = int(input())
# 색종이를 붙인 위치

cnt = 0
# 색종이가 도화지 밖으로 나가는 경우 x
# 색종이는 10 * 10 으로 크기가 고정임.
for _ in range(n):
    l, b = map(int, input().split())
    for i in range(l, l + 10):
        for j in range(b, b + 10):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                cnt += 1

print(cnt)