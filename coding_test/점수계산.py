점수계산
n=int(input())
array=list(map(int,input().split()))
target=0
score=0

for i in range(len(array)):
    if array[i]==0:
        target=0
        continue 
    target+=1
    score+=target

print(score)
