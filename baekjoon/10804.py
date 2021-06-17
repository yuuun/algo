#idx가 1부터 시작한다는 점과 tmp[0]과 tmp[-1]를 고려하지 않아서 해맸음
arr = [str(i) for i in range(0, 21)]
for _ in range(10):
    a, b = map(int, input().split())
    tmp = arr[a : b + 1]
    for idx in range(len(tmp)):
        arr[a + idx] = tmp[-idx - 1]
print(' '.join(arr[1:]))