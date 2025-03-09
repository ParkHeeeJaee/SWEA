'''
정수로 된 id
출입시 id 저장
이후 검사 -> id 두번 = in, out / 한번 in 이후 out없음
나가지 않은 사람 1명 있다고 가정 했을때, 그 사람의 id
pop? 요런거 쓰면 되지 않나?
들어온 값과 같은 값이 있으면 pop 형식으로 풀 수 있다고 생각

xor 연산자 사용해서 어떻게 풀어볼 수 있는지 생각
xor 연산 사용 - > 그냥 이중 for 문으로 일치하는 것 xor 연산하기? <- xor 연산인가?
특정 수로 xor 연산 두번 하면 원래값으로 돌아옴
'''
# t  = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     lst = list(map(int, input().split()))
#     ans = 0
#     for i in lst:
#         ans ^= i
#     print(f'#{tc} {ans}')

print(~4)

print(bin(4))
print(bin(-5))