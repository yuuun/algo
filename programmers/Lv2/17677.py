def split_str(st):
    string = []
    for i in range(0, len(st) - 1):
        if 'a' <= st[i] <= 'z' and 'a' <= st[i + 1] <= 'z':
            string.append(st[i] + st[i + 1])
    return string

def solution(str1, str2):
    str1, str2 = split_str(str1.lower()), split_str(str2.lower())
    if str1 == [] and str2 == []:
        return 65536
    
    str1.sort(), str2.sort()
    inter = 0
    j = 0
    for i in range(len(str1)):
        for k in range(j, len(str2)):
            if str1[i] == str2[k]:
                inter += 1
                j = k
                break
    union = len(str1) + len(str2) - inter
    
    return int(inter * 65536 / union) 

print(solution('FRANCE', 'french'))
print(solution("E=M*C^2", "e=m*c^2"))
print(solution('aa1+aa2', 'AAAA12'))