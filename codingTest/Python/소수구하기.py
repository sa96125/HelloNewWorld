# 소수구하기
# 어떤 자연수 N이 주어졌을 때
# 1~N 까지의 소수의 갯수를 구하여라.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

n = int(input())
cnt = 0
value = 0

for i in range(2, n):
    for j in range(1, i+1):
        if i % j != 0:
            break
        if i % j == 0:
            cnt += 1
        if cnt == 2:
            value += 1
            cnt = 0
            break

print(value)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: 자기자신보다 작은 값으로 나눠지지 않는 숫자를 찾는다. (1 제외)

# 문제:
#   N이 최대 20만개이므로 시간복잡도 O(n**2)로 풀면 시간 초과 판정이다. 그렇다면 n< something <logn로 해결해야한다.

# 해결:
#   에스테라토스의 체라는 수학알고리즘을 사용해야 했다.
#   생전 첨 들어본다. 이 공식의 시간복잡도는 O(Nlog(logN))으로 딱 20만개가 가능한정도의 그래프를 근사치를 가진다.
#   문제를 어떻게든 풀게 만드는 구나 싶었다.

# 느낀점:
#   수학공부를 해야한다고 느낀게 머신러닝에서 선형대수학 HTML에서 미분적분, 중력법칙등을 적용해야 원하는 값을 얻는 경우가 많아졌다.
#   수학적 알고리즘이 오류를 줄아고 신뢰도를 높히는 아주 중요한부분에 속하므로 꾸준히 공부해야겠다.
