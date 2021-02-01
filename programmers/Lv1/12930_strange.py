def solution(s):
    s = s.split(" ")
    answer = ""
    for word in s:
        for i in range(0, len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "
    return answer[:-1]


print(solution("try helloo worldd"))
print(solution("Hello eVeryone"))