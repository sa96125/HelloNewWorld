# 소수구하기
# 어떤 자연수 N이 주어졌을 때 
# 1~N 까지의 소수의 갯수를 구하여라.

# n=int(input())
# cnt=0
# value=0

# for i in range(2,n):
#     for j in range(1,i+1):
#         if i%j!=0:
#             break
#         if i%j==0:
#             cnt+=1
#         if cnt==2:
#             value+=1
#             cnt=0
#             break;

# print(value)


# 풀이:
# 시간복잡도 O(n**2) 
# 소수를 찾아서 카운팅하는 문제 easy 

# 문제점:
# N이 최대 20만개이므로 시간복잡도 O(n**2)로 풀면 시간 초과 판정이다 ㅠ
# 그렇다면 n< something <logn로 해결해야한다.

# 해결방법:
# 에스테라토스의 체라는 수학알고리즘을 사용해야 했다.
# 생전 첨 들어본다. 이 공식의 시간복잡도는 O(Nlog(logN))으로 딱 20만개가 가능한정도의 그래프를 근사치를 가진다.
# 문제를 어떻게든 풀게 만드는 구나 싶었다.
