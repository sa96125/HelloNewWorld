# 스토쿠 검사
# 스토쿠는 매우 간단한 숫자 퍼즐이다. 9*9 크기의 보드가 있을 때 ,
# 각 행과 각열, 그리고 9개의 3*3크기의 보드에 1부터 9까지의 숫자가 중복없이 나타나도록 보드를 채우면 된다.
# 완성된 스토쿠가 주어질 때, 문제를 정확하게 풀면 yes 아니라면 no 를 출력하는 프로그램을 작성하시오.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

BOARD_SIZE = 9
cash = [0]*10
checkFail = 0

board = [list(map(int, input().split() for _ in range(BOARD_SIZE)))]

for i in range(BOARD_SIZE):
    # ------------------------행검사
    for j in range(BOARD_SIZE):
        cash[board[i][j]] = 1

    # sum(cash)!=9
    for k in range(len(cash)):
        if cash[k] == 0:
            checkFail = 1
            break
    # 한줄 마다 발견하면 브레이크
    if checkFail == 1:
        break
    cash.clear

    # ------------------------열검사
    for j in range(BOARD_SIZE):
        cash[board[j][i]] = 1

    for k in range(len(cash)):
        if cash[k] == 0:
            checkFail = 1
            break
    # 한줄 마다 발견하면 브레이크
    if checkFail == 1:
        break
    cash.clear

    # ------------------------3*3검사

for i in range(3):
    for j in range(3):
        for k in range(3):
            for s in range(3):
                cash[board[k+3*i][s+3*j]]
                if sum(cash) != 9:
                    chckFair = 1
                    break
            if chefckFail == 1:
                break
        if chefckFail == 1:
            break
    if chefckFail == 1:
        break

if checkFail == 0:
    print("Yes")
else:
    print("No")


# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: 중복되는 값에 대해서 체크하는 경우기 때문에 따로 메모리를 할당해서 값을 넣고 체크하도록한다.

# 문제:
#   전체 스도쿠 판에서 9개의 3*3배열의 대한 효율적인 검사방법을 생각하는데 시간이 오래 걸림.
#   딱봐도 노가다, 지저분한 코드가 너무 많음

# 해결:
#   4중포문으로 3*3문을 처리하였다.어짜피 갯수가 엄청작기에 상관없으니. 이것도 맞는 방법;(
#   값을 찾을 때 브레이크로 빠져나가는 코드가 너무 지져분하다 함수를 따로 선언하여 return

# 느낀점:
#   문제해결할 때 항상 풀이를 하면서 더 좋은 방법이 있을거라는 생각을하는데 코딩테스트는 시간제한이 있다.
#   그리고 딱히 그 방법이 바로 떠오르지 않는다면 실력이 부족하다는 뜻이기때문에
#   노가다라고 생각할지라도 일단 풀고 난 다음 생각하는게 좋을 것 같다.
