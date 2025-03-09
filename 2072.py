'''
10개의 수를 입력 받아, 홀수만 더한 값을 출력
각 수는 0 <= x <= 10000
'''

t = int(input())
for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    sum_odd = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            sum_odd += numbers[i]

    print(f'#{tc} {sum_odd}')