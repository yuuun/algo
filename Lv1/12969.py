def solution(a, b):
    answer = ""
    tmp = "*" * a
    for _ in range(b):
        answer += tmp + "\n"
    return answer[:-1]
    