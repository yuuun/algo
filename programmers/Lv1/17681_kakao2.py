def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        app = set(to_binary(n, a1) + to_binary(n, a2))
        ans = ""
        for a in range(n):
            if a in app:
                ans += "#"
            else:
                ans += " "
        answer.append(ans[::-1])
    return answer

def to_binary(n, k):
    ans = []
    cnt = 0
    while(k != 0):
        if k % 2 == 1:
            ans.append(cnt)
        k //= 2
        cnt += 1
    return ans
    
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))