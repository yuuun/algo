from collections import defaultdict
def solution(clothes):
    clothes_list = defaultdict(int)
    for v1, key in clothes:
        clothes_list[key] += 1
    
    answer = 1
    for i in clothes_list.values():
        answer *= (i + 1)

    return answer - 1

if __name__=="__main__":
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))