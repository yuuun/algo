import math

if __name__ == "__main__":
    
    min_value, max_value = map(int, input().split())

    min_sqrt = math.ceil(math.sqrt(min_value) if min_value > 3 else 1) ** 2
    print(min_sqrt)
    max_sqrt = math.floor(math.sqrt(max_value)) ** 2
