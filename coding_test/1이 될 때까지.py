# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 다음 두 과정중 하나만 선택하여 반복적으로 수행하려고 합니다.
# 단, 두번째 연산은 나누어떨어질때만 선택할 수 있습니다.
# 1. 1을 뺀다.
# 2. K로 나눈다.

# N과 K가 주어질 때 N이 1이 될 때까지의 수행해야하는 최소 횟수를 구하는 프로그램을 작성하세요.


n, k = map(int, input().split())
cnt = 0

while(True):
    if k > n:
        break
    if n % k != 0:
        cnt += n-(n//k)*k
        n = (n//k)*k
    else:
        n = n//k
        cnt += 1

cnt += n-1
print(cnt)
