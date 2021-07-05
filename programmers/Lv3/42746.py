#TBD
def solution(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True)
    for idx, numbs in enumerate(numbers[:-1]):
        if numbs[:-1] == numbers[idx + 1]:
            numbers[idx + 1], numbers[idx] = numbers[idx], numbers[idx + 1]
    return ''.join(numbers)
