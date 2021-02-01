T = int(input())

day_list =  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T+1):
    fig = input()
    ans = fig[:4]   #year
    mon = int(fig[4:6])
    day = int(fig[6:8])
    if mon > 0 and mon < 13:
        ans += "/" + '{0:02}'.format(mon)
        if day <= day_list[mon]:
            ans += "/" + '{0:02}'.format(day)
        else:
            ans = "-1"
    else:
        ans = "-1" 
    print("#" + str(t) + " " + ans)
