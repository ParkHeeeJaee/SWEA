s = input().strip()
n = len(s)
is_palindrome = 1  # 기본적으로 팰린드롬이라고 가정

for i in range(n // 2):  # 문자열 길이의 절반만 체크하면 됨
    if s[i] != s[n - i - 1]:  # 앞뒤가 다르면 팰린드롬 X
        is_palindrome = 0
        break

print(is_palindrome)
