'''
n 개의 숫자로 구성된 숫자열 ai
m bj
숫자열 움직여서 인덱스 곱하고 더한 후 최댓값 출력
'''

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    
    ai = list(map(int, input().split()))

    bj = list(map(int, input().split()))

    # 고려해야 할 것. n과 m 중 어떤게 큰가?
    max_val = 0
    # n이 m보다 작게 설정
    if n > m:
        ai, bj = bj, ai
        n, m = m, n

    # 큰 리스트와 작은 리스트의 차이만큼 증가
    for s in range(m-n+1):
        val = 0

        # 작은 리스트의 길이만큼 반복
        for i in range(n):
            val += ai[i] * bj[i + s]
        
        # 최댓값 갱신
        if val > max_val:
            max_val = val
    
    print(f'#{tc} {max_val}')