### 최소 스패닝 트리 - 처음 하는 유형
#https://hillier.tistory.com/54
v, e = map(int, input().split())

'''
간선이 적을 경우, Kruskal, 많을 경우 Prim 알고리즘
Kruskal: 간선들을 정렬, 간선이 잇는 두 정점의 root찾기, 다르다면 하나의 root로 바꾸어 연결
Prim: 임의의 정점 선택, 해당 정점에서 갈 수 있는 간선을 minheap에 넣기, 최소값을 뽑아 해당 정점을 방문 안하면 선택
'''

#kruskal
def kruskal():
    Vroot = [i for i in range(v + 1)]
    Elist = []
    for _ in range(e):
        Elist.append(list(map(int, input().split())))
    Elist.sort(key=lambda x: x[2])

    def find(x):
        if x != Vroot[x]:
            Vroot[x] = find(Vroot[x])
        return Vroot[x]
    answer = 0
    for s, e, w in Elist:
        sRoot = find(s)
        eRoot = find(e)
        if sRoot != eRoot:
            if sRoot > eRoot:
                Vroot[sRoot] = eRoot
            else:
                Vroot[eRoot] = sRoot
            answer += w
    print(answer)

def prim():
    visited = [False] * (V + 1)
    Elist = [[] for _ in range(V + 1)]
    heap = [[0, 1]]
    for _ in range(E):
        s, e, w = map(int, input().split())
        Elist[s].append([w, e])
        Elist[e].append([w, s])
    answer = 0
    cnt = 0

    while heap:
        if cnt == v:
            break
        w, s = heapq.heappop(heap)
        if not visited[s]:
            visited[s] = True
            answer += w
            cnt += 1
            for i in Elist[s]:
                heapq.heappush(heap, i)
    print(answer)