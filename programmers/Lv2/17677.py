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
    
    union = len(str1) + len(str2)
    inter = 0
    for s1 in str1:
        if s1 in str2:
            inter += 1
            str2.remove(s1)
    
    union = union - inter
    
    return int(inter * 65536 / union) 

print(solution('FRANCE', 'french'))
print(solution("E=M*C^2", "e=m*c^2"))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('aabbc', 'abbde'))