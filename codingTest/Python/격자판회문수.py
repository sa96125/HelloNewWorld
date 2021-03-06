# 격자판 회문수
# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서
# 가로뱡향 또는 세로방향으로 길이 5의 회문수가 몇개 있는지 구하는 프로그램을 작성하시오.
# 회문수는 121과 같이 앞에서부터 읽으나 뒤에서 부터 읽으나 같은 수를 말합니다.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

legnth_of_compare = 5
cnt = 0

board = [list(map(int, input().split())) for _ in range(7)]

for row in range(3):
    for col in range(3):
        for i in range(legnth_of_compare):
            if board[row][col+i] != board[row][col+legnth_of_compare-1-i]:
                continue
            elif board[col+i][row] != board[col+legnth_of_compare-1-i][row]:
                continue
            else:
                cnt += 1

print(cnt)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이:
#   10분안에 해결 할 수 있었던 문제이다.
#   이전에 4중포문의 필요성과 회문문자열에 대해서 문제를 해결해 보았기 때문에 어려움 없이 풀이 할 수 있었다.

# 문제: 생략

# 해결: 생략

# 느낀점:
#   이때까지 시간복잡도에 대한 압박감으로 2중포문 3중포문의 경우의 수를 따져 풀이법을 찾았는데
#   이렇게 크지않은 경우의 수가 있을 경우에는 아무리 3중 4중문이라고 하더라도 코드 길이를 줄일 수 있는 아주 좋은 해결책이 된것 같다.
