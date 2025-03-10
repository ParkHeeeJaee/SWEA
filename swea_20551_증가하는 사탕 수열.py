# '''
# a < b < c 성립 해야함.
# 모든 상자에는 1개 이상의 사탕이 있어야 함.

# '''
# t= int(input())
# for tc in range(1, t+1):
#     # 변수가 3개 뿐이기 때문에, 리스트를 쓸 필요가 있나? x

#     a, b, c = map(int, input().split())

#     if b < 2 or c < 3:
#         print(f'#{tc} -1')
#         continue

#     cnt = 0

#     if b >= c:
#         cnt += b - (c - 1)
#         b = c - 1
    
#     if a >= b:
#         cnt += a -(b-1)
#         a = b - 1

#     print(f'#{tc} {cnt}')

'''
상자 3개 a, b, c
a < b < c
a,b,c != 0
-= 가능
'''

t = int(input())
for tc in range(1, t+1):
    a, b, c = map(int, input().split())
    # abc가 0 이 되면 안됨 - > b는 2 이상, c는 3 이상이여야함.
    if b < 2 or c < 3:
        print(f'#{tc}', -1)