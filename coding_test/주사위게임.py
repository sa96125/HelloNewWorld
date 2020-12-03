주사위게임

n=int(input())
a=[]
target=[]

for i in range(n):
    number_=list(input().split())
    a.append(number_)
    
for i in range(n):
    for j in range(3):
        if a[i][0] == a[i][1] == a[i][2]:
            target.append(int(a[i][0])*1000+10000)
        elif a[i][0] == a[i][1] or a[i][0] == a[i][2]:
            target.append(int(a[i][0])*100+1000)
        elif a[i][1] == a[i][2]:
            target.append(int(a[i][1])*100+1000)
        else:
            target.append(int(a[0][0])*100)

target.sort()
print(target[-1])