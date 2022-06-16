def production(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in production(arr, r - 1):
                yield [arr[i]] + j

def solution(word):
    words = []
    for i in range(1, 6):
        for c in production(['A', 'E', 'I', 'O', 'U'], i):
            words.append(''.join(list(c)))
    words.sort()
    return words.index(word) + 1