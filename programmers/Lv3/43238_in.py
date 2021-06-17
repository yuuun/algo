#binary search?! - 이해 못했...
def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left < right:
        mid = (left + right) // 2
        total = 0
        for t in times:
            total += mid // t
        if total >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer

if __name__=="__main__":
    print(solution(6, [7, 10]))