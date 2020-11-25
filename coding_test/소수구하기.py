# 소수구하기
# 어떤 자연수 N이 주어졌을 때 
# 1~N 까지의 소수의 갯수를 구하여라.

n=int(input())
cnt=0
value=0

for i in range(2,n):
    for j in range(1,i+1):
        if i%j!=0:
            break
        if i%j==0:
            cnt+=1
        if cnt==2:
            value+=1
            cnt=0
            break;

print(value)


# 풀이:
# 시간복잡도 O(n*2)
# 소수를 찾아서 카운팅하는 문제 easy 
# 문제점:
# X
# 해결방법:
# X