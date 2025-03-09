t = int(input())  # 테스트 케이스 개수 입력

def preorder(t):
    global cnt  # 전역 변수 cnt 사용 선언
    if t:  # 노드가 존재하면 실행
        cnt += 1  # 현재 노드를 방문했으므로 카운트 증가
        
        preorder(cleft[t])  # 왼쪽 자식 방문
        preorder(cright[t])  # 오른쪽 자식 방문

# 트리 안에 속한 노드의 개수 찾기 -> 트리를 순회하며 개수를 셈
# 순회하며 리스트에 추가하면 중복 노드가 들어갈 가능성이 있음
# 방문 처리를 하려면 set을 쓰거나 방문 체크 리스트를 사용할 수도 있음
# 하지만 현재는 단순히 cnt += 1 방식으로 해결

for tc in range(1, t+1):  # 각 테스트 케이스 처리
    e, n = map(int, input().split())  # 간선 개수 e, 서브트리 루트 n 입력
    cleft = [0] * (e+1+1)  # 왼쪽 자식 저장 배열 (노드 번호 범위 고려)
    cright = [0] * (e+1+1)  # 오른쪽 자식 저장 배열

    arr = list(map(int, input().split()))  # 부모-자식 관계 입력

    for i in range(e):  # 간선 개수만큼 반복하여 트리 구성
        p = arr[i * 2]  # 부모 노드
        c = arr[i * 2 + 1]  # 자식 노드

        if cleft[p] == 0:  # 왼쪽 자식이 비어있으면 왼쪽에 저장
            cleft[p] = c
        else:  # 왼쪽이 이미 차 있으면 오른쪽에 저장
            cright[p] = c

    cnt = 0  # 서브트리 내 노드 개수 초기화

    preorder(n)  # 주어진 노드 n을 루트로 서브트리 개수 계산
    
    print(f'#{tc} {cnt}')  # 결과 출력
