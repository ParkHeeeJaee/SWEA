'''
10개의 수를 입력받아, 평균값 출력
! 소수점 첫째 자리에서 반올림한 정수 출력
0 <= x <= 10000
'''

t = int(input())
for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    
    # 소수점에서 반올림 하기 위해 round 함수 사용
    # int 사용시 반올림이 아니라 소수 부분을 버려버림
    result = round(sum(numbers) / n)

    print(f'#{tc} {result}')
