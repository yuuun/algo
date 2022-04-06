def solution(bridge_length, weight, truck_weights):
    t = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        t += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return t
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10] * 10)) # 110