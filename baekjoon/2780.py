t = int(input())
for _ in range(t):
    elec = [1 for _ in range(10)]
    for _ in range(int(input()) - 1):
        e = elec[:]
        elec[1] = e[2] + e[4]
        elec[2] = e[1] + e[3] + e[5]
        elec[3] = e[2] + e[6]
        elec[4] = e[5] + e[1] + e[7]
        elec[5] = e[2] + e[4] + e[6] + e[8]
        elec[6] = e[3] + e[5] + e[9]
        elec[7] = e[4] + e[8] + e[0]
        elec[8] = e[5] + e[7] + e[9]
        elec[9] = e[6] + e[8]
        elec[0] = e[7]
    print(sum(elec) % 1234567)