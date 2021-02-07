#failed!!
def solution(name):
    print(name)
    cnt = 0
    if len(set(name)) == 1:
        return 0 if name[0] == 'A' else getAsc(name[0])

    candidates = []
    idx = 1
    while(idx < len(name)):
        if name[idx] == 'A':
            tmp = getNumOfA(name, idx)
            candidates.append([idx, idx + tmp])
            idx += tmp
        else:
            idx += 1

    if candidates == []:
        return getSumChar(name) + len(name) - 1
    else:
        ans_list = []
        for can in candidates:
            start = can[0] - 1
            end = len(name) - can[1]
            cnt = min(2 * start + end, start + 2 * end)
            
            print(can[0], can[1], start, end, cnt)
            ans_list.append(cnt)

        return getSumChar(name) + min(ans_list)

def getSumChar(name):
    cnt = 0
    for n in name:
        if n != 'A':
            cnt += getAsc(n)
    return cnt

def getAsc(n):
    asc_A = ord('A')
    tmp = ord(n) - asc_A
    asc_Z = ord('Z')
    asc__ = int((ord('Z') - ord('A')) / 2)
    if tmp <= asc__:
        return tmp
    else:
        return asc_Z - ord(n) + 1

def getNumOfA(name, start):
    end = len(name) - start
    for idx in range(start, len(name)):
        if name[idx] != 'A':
            return idx - start
    return end


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("AAABB"))
print(solution("AABBAA"))
print(solution("ABBBA"))
print(solution("AABAABA"))
print(solution("AABAABA"))
print(solution("ABABAAAAABA"))
print(solution("BBBAAAB"))
print(solution("ABAAAAAAAAABB"))
print(solution("ABABAAAAAB"))
print(solution("ABABAAAAAAABA"))
print(solution("BABAAAAB"))
print(solution("BBBAAB"))
print(solution("BBAABAAAAB"))