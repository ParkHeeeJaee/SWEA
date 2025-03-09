t = int(input())
for tc in range(1, t+1):
    lst = [2, 3, 5, 7, 11]
    n = int(input())
    nums = []

    for i in lst:
        cnt = 0

        while n % i == 0:
            n //= i
            cnt +=1
        nums.append(cnt)

    print (f'#{tc}', *nums)