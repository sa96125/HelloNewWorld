# 정렬된리스트합치기
# 오름차순으로 이미 정렬된 숫자 덱이 있다.
# 서로다른 덱을 합친 다음 오름차순 정렬을 하고 최종적으로 완성된 덱을 출력하는 프로그램을 작성하여라.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

p1, p2 = 0, 0
# p1=p2=0
cardsOld = []
sorted_list = []

for _ in range(1):
    cardsNew = list(map(int, input().split()))

    for in range
       if cardsOld[p1] <= cardsNew[p2]:
            sorted_list.append(cardsOld[p1])
            p1 += 1
            if p1 == len(cardsOld):
                break

        else:
            sorted_list.append(cardsNew[p2])
            p2 += 1
            if p2 == len(cardsNew):
                break

    if p1 < len(cardsOld):
        sorted_list = sorted_list+cardsOld[p1:]

    elif p2 < len(cardsOld):
        sorted_list = sorted_list+cardsOld[p2:]

    cardsOld = sorted_list
    sorted_list.clear()
ß
print(sorted_list)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: sort()함수를 이용하여 해결.

# 문제:
#   큰 숫자가 들어왔을 때 이미정렬된 숫자를 퀵정렬 한다면 시간복잡도가 상당히 비효율적이다.
#   리스트에 남은 숫자들을 새로운 리스트에 어떻게 붙일 것인가?

# 해결:
#   정렬된 값의 특성을 살려서 앞에서 부터 차례대로 비교하여 효율성을 높힌다.
#   슬라이스[]와 + 연산을 사용하여 쉽게 리스트에 추가 할 수 있었다.

# 느낀점:
#   시간복잡도와 파이썬의 sort()는 퀵정렬을 사용한다는 것을 알고 있었음에도 불구하고 퀵정렬의 단점에 대해서 생각하지 않았다.
#   아무생각없이 API를 사용할 때의 안좋은 예를 보여준다. 바로 이전에서 우려했던 부분인데 이렇게 일깨워주니 고맙다.
