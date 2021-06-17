#greedy algorithm
n_edge = int(input())
edge_list = list(map(int, input().split()))
node_list = list(map(int, input().split()))

#최초 1회에 기름 넣어야 됨
ans = edge_list[0] * node_list[0]
min_node = node_list[0]

for edge, node in zip(edge_list[1:], node_list[1:-1]):
    #이전 장소에서 기름값이 더 비쌀 경우에는 현지 노드의 기름 값으로 변경해줌
    if min_node > node:
        min_node = node
    
    ans += min_node * edge

print(ans)