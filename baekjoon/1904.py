#dynamic problem
#recursion error
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return ((solution(n - 1)) % 15746 + (solution(n - 2)%15746))% 15746
def solution2(n):
    ans = [0, 1, 2]
    for i in range(3, n + 1):
        ans.append(((ans[i - 1]) % 15746 + (ans[i - 2]) % 15746)% 15746) 
    return ans[n]

if __name__ == "__main__":
    inp = int(input())
    #print(solution(inp))
    print(solution2(inp))


