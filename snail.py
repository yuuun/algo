dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def snail(n):
    arr = [[1] * n for _ in range(n)]
    k = n // 2
    size_map = n ** 2
    x, y = k, k
    cnt, idx = 1, 2 # 이동할 개수, 지도에 적힐 현 시점의 index
    
    while idx < size_map:
        for i in range(4): # direction
            t = 0
            while t < cnt and size_map > idx:
                x += dxy[i][0]
                y += dxy[i][1]
                arr[x][y] = idx
                t += 1
                idx += 1
            if i in [1, 3]:
                cnt += 1
    arr[0][0] = size_map
    return arr

print(snail(7))