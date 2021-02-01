import copy
def solution(routes):
    #answer = 0
    routes.sort(key=lambda routes: routes[1])
    tmp = copy.deepcopy(routes)
    ans_list = []
    rou_list = [False for i in range(len(routes))]

    for idx, rout in enumerate(routes):
        if rou_list[idx]:
            continue
        else:
            rou_list[idx] = True
            ans_list.append(rout[1])
            tmp.remove(rout)
            for t in tmp[:]:
                if t[0] <= rout[1] and t[1] >= rout[1]:
                    tmp.remove(t)
                    rou_list[routes.index(t)] = True
    return len(ans_list)

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
print("")
print(solution([[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]))