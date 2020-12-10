# 곳감과 모래시계
# 현수는 곳감을 만들기 위해 마당에 말리고 있습니다.
# 마당은 N*N격자판으로 되어있으며, 해에 위치에 따라 감이 잘 마르지 않습니다.
# 2 0 3 로 값이 주어지면 2행의 0(왼쪽방향)으로 3칸으로 위치를 변경하여 감이 잘 마르게 합니다.
# 단 2번째에서 1이면 오른쪽으로 도는 옵션이 있습니다.
# 다음과 같은 마당이 있을 때, M 개의 회전 명령이 있을 때 모래 시계 영역에서는 감이 몇개 있는지 출력하시오.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

board = []
change = []
tmp = 0
total_fruit = 0

n = int(input())
for _ in range(n):
    board.append(list(map(int, input().split())))

m = int(input())
for _ in range(m):
    change.append(list(map(int, input().split())))

for i in range(m):
    if change[i][1] == 0:
        for _ in range(change[i][2]):
            tmp = board[change[i][0]].pop(0)
            board[change[i][0]].append(tmp)
    else:
        for _ in range(change[i][2]):
            tmp = board[change[i][0]].pop()
            board[change[i][0]].insert(0, tmp)

for i in range(n):
    if i < n//2:
        for j in range(n-2*i):
            total_fruit += board[i][j+i]

    else:
        for j in range(2*(i-n//2)+1):
            total_fruit += board[i][j-i+n]

print(totalFruit)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: 2중 포문을 사용하여 인덱스의 규칙성을 찾아내는 문제

# 문제: 회전하는 방법

# 해결:
#   insert, pop, remove, append과 같은 리스트 함수에 대한 이해가 필요했다.

# 느낀점:
#   2차원 배열의 규칙성 범위에 대한 공식을 찾아내는 것을 이전 문제에서 머리아프게 다뤘더니 이번 문제에서는 스무스하게 해결했다.
#   이전 문제에서 깨달을 점을 바탕으로 좀더 응용된 문제를 빠르게 해결할 수 있어서 너무 좋았다.
#   하지만, 2차원문제는 코테에서도 많이 등장하는지라 매일 아침 뇌의 CPU에 넣고 실행시켜야 겠다:)
