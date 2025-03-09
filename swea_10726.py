

# m의 우측 n개를 확인할 예정
# def solution():
#     target == m
#     for _ in range(n):
#         if target & 0x1 == 0:
#             return False
#         target = target >> 1

def solution():
    #n 개의 1을 구함
    mask = (1 << n) - 1
    result = (m & mask) == mask
    return result


t = int(input)
for tc in range(1, t+1):
    n, m = map(int, input().split())
    result = solution()


