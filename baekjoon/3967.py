abc_dic = {}
abc = []
for i, j in zip(range(27), range(65, 92)):
    abc_dic[chr(j)] = i
    abc.append(chr(j))

visited = [False] * 26

hexa = []
n_empty = 12
for _ in range(5):
    letter = [i for i in list(input()) if i != '.']
    hexa.append(letter)
    for l in letter:
        if l == 'x':
            n_empty -= 1
            continue
        visited[abc_dic[l]] = True

def dfs(cur, depth):
    if depth == n_empty:
        return
print(visited, hexa)