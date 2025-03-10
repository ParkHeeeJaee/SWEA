'''
전봇대 두개
n개의 전성으로 연결
끝점이 같은 경우 x, 교차하는 경우는 존재
세 개 이상의 전선이 하나의 점에서 만나는경우 x
총 몇 개의 교차점이 존재하는가?
'''

t = int(input())

for tc in range (1, t+1):

wires = []
ans = 0

for _ in range(n):
    start, end = map(int, input().split())

    for prev_start, prev_end in wires:
        if start > prev_start and end < prev_end:
            ans += 1

        if start < prev_start and end > prev_end:
            ans += 1

    # 목록에 전선을 추가
    wires.append(start, end)
print(t'#{tc} {ans}'