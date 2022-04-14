def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = [cities[0]]
    if cacheSize == 0:
        answer = 5 * (len(cities))
    else:
        answer = 5
        for city in cities[1:]:
            if len(cache) < cacheSize:
                if city in cache:
                    cache.pop(cache.index(city))
                    answer += 1
                else:
                    answer += 5
            elif city in cache:
                cache.pop(cache.index(city))
                answer += 1
            else:
                cache.pop(0)
                answer += 5
            cache.append(city)
    return answer
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
