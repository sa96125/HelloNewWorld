# 수열의 합
# N개의 수로 된 수열이 있다. 이 수열의 i 번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

n, m = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(n):
    sum = num[i]
    for j in range(i+1, n):
        if sum < m:
            sum += num[j]
        elif sum > m:
            break

        if sum == m:
            cnt += 1
            break

    print(cnt)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: 순서대로 기준값과 그외의 값들의 연산을 진행하므로 for ** 2 문으로 문제 해결한다.

# 문제: 정답은 출력값이 5인데 4까지나옴. 분명히 계산상으로는 맞음.

# 해결:
#   cnt+1을 하는 부분을 앞쪽에 두어서 마지막루프에서 값을 더하고도 cnt+1을 하지 못하는 상황이 발생했다.
#   판단 값을 마지막에 둔다.

# 느낀점:
#   이번문제로 깨달은 점은 포문을 돌때 특정조건 예외처리조건을 앞에 배치하는 습관때문에 이번에도 앞쪽에 결과를 처리하게 했다.
#   이는 엄연히 다른문제로 포문에서 결과값처리를 앞에 두면 포문을 돌지 못하는 현상이 발생한다.
