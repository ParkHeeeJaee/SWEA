'''
10개의 평점
a+, a0, a-, b+ .... d0
총점 = 중간고사 35% 기말고사 45% 과제 20%
평점 = 총점이 높은 순서대로 부여
각각의 평점은 같은 비율로 부여 가능
학점을 알고싶은 k 학생의 번호
k번째 학생의 학점을 출력
'''

t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C', 'C-', 'D0']

for tc in range(1, t+1):
    # n:학생수, k: 표적 학생 번호
    n, k = map(int, input().split())
    # n 명의 점수 리스트를 이차원 배열
    # scores = [list(map(int, input().split())) for _ in range(n)]

    scores = {}

    for i in range(1, n+1):
        m, f, hw = map(int, input().split())
        total_score = (m * 35) + (f * 45) + (hw * 20)
        scores[i] = total_score

    sorted_scores = list(scores.items())

    sorted_scores.sort