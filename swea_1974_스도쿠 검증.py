'''
가로 세로 9칸
1~9까지 숫자 채워야함
같은 줄(가로, 세로)에 중복되는 숫자 x
3 * 3 작은 격자 안의 숫자 겹치면 x
겹치는 숫자가 없을경우 1, 겹치면 0
'''

t = int(input())
for tc in range(1, t+1):
    grid = [list(map(int, input().split())) for _ in range(9)]
    check_sum = sum([1,2,3,4,5,6,7,8,9])
    qed = 1

    # 가로줄, 세로줄 검사
    for i in range(9):
        # set 만들어서 중복 검사
        row_set = set()
        col_set = set()
        for j in range(9):
            # 각각 set에 올림
            row_set.add(grid[i][j])
            col_set.add(grid[j][i])
        # 조건에 부합하지 않으면 qed 0 주고 break
        if row_set != set(range(1, 10)) or col_set != set(range(1, 10)):
            qed = 0
            break
    # 이전이 True면 실행
    if qed:
    # 작은 격자
    # 0~8 까지, 3개 단위로 끊어서 진행
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                grid_set = set()
                for x in range(3):
                    for y in range(3):
                       grid_set.add(grid[i+x][j+y])
                if grid_set != set(range(1, 10)):
                    qed = 0
                    break
            if qed:
                break

    print(f'#{tc} {qed}')