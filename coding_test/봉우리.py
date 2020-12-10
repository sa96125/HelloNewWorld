# 봉우리
지도 정보가 n*n격자판에 주어 집니다. 각 격자에는 그 지역의 높이가 쓰여 있습니다.
각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리 지역이 몇개 있는지 알아내는 프로그램을 작성하시오.
단, 격자의 가장자리는 0으로 초기화 되었다고 가정한다.

# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

n = int(input())
board = [0]
mountainTop = 0

for _ in range(n):
    board.append(list(map(int, input().split())))
# board=[list(map(int,input().split())) for _ in range(n) ]

board.insert(0, [0]*n)
board.append([0]*n)
for i in range(board):
    i.insert(0, 0)
    i.append(0)

for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] > board[i-1][j] and board[i][j] > board[i][j-1] and board[i][j] > board[i+1][j] and board[i][j] > board[i][j+1]:
            # if all(board[i][j] > board[i+dx[k]][j+dy[k]] for k in range(4))
            mountainTop += 1

print(mountainTop)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이:
#   가장자리를 0으로 초기화는 인덱스를 벗어나면 제외한다는 의미.
#   2차원배열 값을 순차적으로 비교해주는 연산만 반복문에 넣으면 된다.
#   추가적으로 이전 값이 봉우리면 continue로 시간복잡도를 줄인다.

# 문제:
#   2차원 판의 배열의 가장자리를 0으로 만들고 싶어도 이미 크기를 정한 배열의 크기를 벗어난 인덱스를 선언할 수가 없다.
#   그렇다면 미리 가장자리가 0인 배열을 선언하고 그안에 입력받은 숫자를 넣어야하는데 어떻게 해야하나...

# 해결:
#  s insert, append함수를 이용

# 느낀점:
#   참조 1.board=[list(map(int,input().split())) for _ in range(n)]
#   참조 2.if all(board[i][j] > board[i+dx[k]][j+dy[k]] for k in range(4))
