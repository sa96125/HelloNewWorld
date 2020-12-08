# 격자판 최대합
# 다음의 5*5격자판에 아래와 같이 숫자가 적혀있습니다.
# 10 13 10 12 15

# ~

# 19 20 30 14 39
# 각 행의 합, 열의 합, 대각의 합중에 가장 큰합을 출력하는 프로그램을 작성하시오.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

n = int(input())
board = []
max_sum = 0
sum1, sum2, sum3, sum4 = 0, 0, 0, 0

for _ in range(n):
    number = list(map(int, input().split()))
    board.append(number)

for i in range(n):
    sum1 += board[i][i]
    sum2 += board[n-1-i][i]
    for j in range(n):
        sum3 += board[i][j]
        sum4 += board[j][i]
    if sum3 > max_sum:
        max_sum = sum3
        sum3 = 0
    elif sum4 > max_sum:
        max_sum = sum4
        sum4 = 0

if sum1 > max_sum:
    max_sum = sum1
elif sum2 > max_sum:
    max_sum = sum2

print(max_sum)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: 2차원 배열의 단순 데이터 계산방법.

# 문제: 1중 포문, 2중포문에서의 값의 차이가 없음.

# 해결: 1중 포문과 2중포문의 비교하는 횟수

# 느낀점:
#   단순한 문제이지만 머리속으로 들어가면 꼬일때가 종종있다.
#   연습하지 않으면 시간이 많이 걸리는데 이런 쉬운문제는 머리속에서 돌리면 바로 계산이 될 수 있게 꾸준히 뇌를 돌려야겠다.
