'''
남남 여여
한방에는 같은 학년
배정할 수 있는 최대 인원 수 k
조건에 맞게 모든 학색을 배정하기 위해 필요한 방의 최소 개수
'''

m = {i: 0 for i in range(1, 7)}
w = {i: 0 for i in range(1, 7)}

n, k = map(int, input().split()) # 학생 수, 배정할 수 있는 최대 인원 수
for _ in range(n):
    s, y = map(int, input().split()) # 성별, 학년
    if s == 1:
        m[y] += 1
    else:
        w[y] += 1

rooms = 0

for i in range(1, 7):
    rooms += m[i] // k
    if m[i] % k != 0:
        rooms += 1
    rooms += w[i] // k
    if w[i] % k != 0:
        rooms += 1

print (rooms)