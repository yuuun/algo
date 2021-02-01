
if __name__ == "__main__":
    MOD = 1000000007
    A = int(input())
    X = int(input())
    times_list = list()

    binary = bin(X)[2:] 

    times_list.append(A)
    for i in range(len(binary) - 1):
        times_list.append(times_list[-1] ** 2 % MOD)
    
    res = 1
    for idx, val in enumerate(binary):
        if val == '1':
            res *= times_list[len(times_list)-idx-1] % MOD
    print(res % MOD)