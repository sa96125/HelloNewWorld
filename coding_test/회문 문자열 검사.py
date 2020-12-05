# 회문 문자열 검사

# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우
# yes를 출력하고 회문 문자열이 아니면 no를 출력하는 프로그램을 작성한다.
# 단, 대 소문자를 구분하지 않는다.

# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

n = int(input())
string_data

for i in range(n):
    string_data = input()
    string_data_capital = string_data.upper()
    for j in range(len(string_data_capital)//2):
        if string_data_capital[j] != string_data_capital[-1-j]:
            print("#%d No" % (i+1))
            break
        else:
            print("#%Yes" % (i+1))
            break


# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이:
# 생략(easy)

# 문제점:
# 생략(easy)

# 해결방법:
# .upper()으로 예외처리 가능하다.

# 느낀점:
# 좀 더 파이썬 스러운 방법으로도 해결 가능하다는 것을 풀이를 보고 알았다.
# 문자열[] == 문자열[::-1] 역순으로 동시에도 비교 가능하니 참고하자.
