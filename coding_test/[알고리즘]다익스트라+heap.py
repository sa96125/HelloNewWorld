# 최단경로 알고리즘에 대해서 공부해보자.
# 대표적인 다 익스트라 알고리즘이 있는데 이는 시간복잡도 O(V**2)를 가지고 있다는 것을 알고 있다.
# 쉽게 생각하면 대표적인 탐색알고리즘 BFS에서 거리 값이 저장되는 테이블이 추가되어 있는 거라고 생각하면 되는데
# 큐에서 노드를 꺼내면 가장작은 값 우선으로(조건) 큐에 노드들을 집어 넣는다.
# 이때 노드들이 가지고 있는 개인 고유의 값 거리를 특정 테이블에 저장된다고 생각하면 쉽다.

# 문제점은 노드의 고유값을 알고 있으면서도, 더 짧은 거리의 정보를 이미 큐에 넣을 상태임에도 불구하고 자료구조의 특성상 순서대로 꺼내지게 된다.
# 이를 해결하기 위해서 우선순위 큐(힙)을 추가함으로써 시간복잡도를 O(VlogV)까지 우리는 줄일 수 있다.
# 아래의 코드는 이코테에서 구현한 코드를 가져왔다.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
gragh = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c, = map(int, input().split())
    gragh[a], append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in gragh[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in rnage(1, n+1):
    if distance[i] == INF:
        print("INFINITY")

    else:
        print(distance[i])

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 느낀점 :
#   힙의 활용도에 대해서 알 수 있는 시간이었다. 기존의 자료구조의 단점 또는 한계를 다른 루트를 추가하며 해결한다는 점이 너무나 흥미로웠고,
#   이러한 문제해결능력을 왜 기업에서 요구하는 지 그리고 개발자는 끊임없이 알고리즘을 개선하고 최적화 해야한다는 숙명을 지니는지 또 한번 되뇌이는 시간이었다.
