# 스토쿠 검사
# 스토쿠는 매우 간단한 숫자 퍼즐이다. 9*9 크기의 보드가 있을 때 ,
# 각 행과 각열, 그리고 9개의 3*3크기의 보드에 1부터 9까지의 숫자가 중복없이 나타나도록 보드를 채우면 된다.
# 완성된 스토쿠가 주어질 때, 문제를 정확하게 풀면 yes 아니라면 no 를 출력하는 프로그램을 작성하시오.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

size_board = 9
sumofColumn = 0
target = 0

board = [list(map(int, input().split())) for _ in range(size_board)]

for i in range(size_board):
    if board[i].sum() != 45:
        target += 1
        break

for j in range(size_board):
    for i in range(size_board):
        sumofColumn += board[i][j]
        if sumofColumn != 45:
            target += 1
            break

for i in range()

if !target:
    print("Yes")
else:
    print("No")


# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이:

# 문제:

# 해결:

# 느낀점:
