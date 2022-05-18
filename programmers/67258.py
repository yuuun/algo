from collections import defaultdict
def solution(gems):
    answer = []
    n = len(set(gems))
    len_max = 1e20
    left = 0
    dic = defaultdict(int)
    for right in range(len(gems)):
        dic[gems[right]] += 1
        right += 1
        while len(dic) == n:
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
            tmp = right - left
            if len_max > tmp:
                answer = [left, right]
                len_max = tmp
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))